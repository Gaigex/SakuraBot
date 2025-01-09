from datetime import date
import discord
from discord import Embed
from cogs.utility.register import check_user_registered
import json

def command(bot):
    @bot.tree.command(name="daily", description="Claim your daily rewards.")
    async def daily(interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        # Checks if user is registered
        if not await check_user_registered(user_id, interaction):
            return

        current_date = date.today()

        # Check if user has claimed daily reward today
        if await Date.check_date(user_id, current_date, interaction):
            return

        user = interaction.user
        nickname = user.nick or user.global_name or user.name

        # Load user data and calculate the daily EXP
        with open("data/userdata.json", "r") as f:
            userdata = json.load(f)

        user_data = userdata["masters"][user_id]
        user_level = user_data["levels"]["level"]
        daily_exp = Calculate.calculate_daily_reward(user_level)

        # Check if the interaction has already been responded to
        if not interaction.response.is_done():
            await interaction.response.send_message(embed=CustomEmbed.daily(nickname, daily_exp))
        else:
            await interaction.followup.send(embed=CustomEmbed.daily(nickname, daily_exp))

        # Give EXP to the user
        await Reward.give_exp(user_id, daily_exp, nickname, interaction)


class CustomEmbed:
    @staticmethod
    def daily(nickname, daily_exp):
        embed = discord.Embed(
            title=f"{nickname}'s Daily Rewards",
            description="To be added.",
            color=0x00FF00 # Green
        )
        embed.add_field(name="EXP", value=f"{daily_exp}")
        return embed
    @staticmethod
    def levelup(nickname, level, current_exp, next_level_exp):
        embed = discord.Embed(
            title="Level Up!",
            description=f"Congratulations, {nickname}! You've leveled up to Level {level}!",
            color=0xFFD700 # Gold
        )
        embed.add_field(name="Current Level", value=f"{level}")
        embed.add_field(name="Next Level Progress", value=f"{current_exp}/{next_level_exp} EXP")
        embed.set_footer(text="Tip: You can view your current progress with /profile!")
        return embed


class Calculate:
    @staticmethod
    def calculate_daily_reward(user_level):
        base_reward = 100  # base daily reward in EXP
        level_multiplier = 0.1  # how much the reward increases per level

        # Calculate reward based on level
        daily_exp = round(base_reward * (1 + (user_level - 1) * level_multiplier))
        return daily_exp


class Reward:
    @staticmethod
    async def give_exp(user_id, exp_to_add, nickname, interaction):
        with open("data/userdata.json", "r") as f:
            userdata = json.load(f)

        user_data = userdata["masters"][user_id]

        # Gives user EXP
        user_data["levels"]["exp"] += exp_to_add

        # Checks if user has leveled up
        current_exp = user_data["levels"]["exp"]
        next_level_exp = user_data["levels"]["next_level_exp"]

        if current_exp >= next_level_exp:
            # Level up the user
            user_data["levels"]["level"] += 1
            user_data["levels"]["exp"] -= next_level_exp
            user_data["levels"]["next_level_exp"] = round(int(next_level_exp * 1.2))
            level = user_data["levels"]["level"]
            current_exp = user_data["levels"]["exp"]
            next_level_exp = user_data["levels"]["next_level_exp"]

            # Send level-up message
            # Check if the interaction has already been responded to
            if not interaction.response.is_done():
                await interaction.response.send_message(embed=CustomEmbed.levelup(nickname, level, current_exp, next_level_exp), ephemeral=True)
            else:
                await interaction.followup.send(embed=CustomEmbed.levelup(nickname, level, current_exp, next_level_exp), ephemeral=True)

        # Save the updated user data back to the file
        with open("data/userdata.json", "w") as f:
            json.dump(userdata, f, indent=4)

class Date:
    @staticmethod
    async def check_date(user_id, current_date, interaction):
        current_date = str(current_date)  # Convert date to string for consistency in the JSON file.

        with open('data/userdata.json', 'r') as file:
            userdata = json.load(file)

        # Check if the user has already claimed their daily reward today
        if current_date == userdata["masters"][user_id].get("last_daily"):
            await interaction.response.send_message(content="You've already received today's daily rewards.", ephemeral=True)
            return True  # Return True to indicate the user already claimed their reward

        # If not claimed yet, update the date
        userdata["masters"][user_id]["last_daily"] = current_date

        # Write the updated data back to the file
        with open('data/userdata.json', 'w') as file:
            json.dump(userdata, file, indent=4)

        return False  # Return False to indicate the user can claim the reward
