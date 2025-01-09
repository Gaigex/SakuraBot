import discord
from discord import Embed
from cogs.utility.register import check_user_registered

def command(bot):
    @bot.tree.command(name="clock_tower", description="Study and work at the Clock Tower.")
    async def clock_tower(interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        if not await check_user_registered(user_id, interaction):
            return
        await interaction.response.send_message(embed=CustomEmbed.clock_tower())

class CustomEmbed:
    @staticmethod # Clock Tower
    def clock_tower():
        embed = Embed(
            title="Clock Tower",
            description="To be added",
            color=0xFFD700  # Yellow
        )
        embed.set_image(url="https://i.ibb.co/MgxW2bb/clocktower.jpg")
        return embed