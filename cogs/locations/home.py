import discord
from discord import Embed
from cogs.utility.register import check_user_registered

def command(bot):
    @bot.tree.command(name="home", description="Craft items and rest your Heroes.")
    async def home(interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        if not await check_user_registered(user_id, interaction):
            return
        await interaction.response.send_message(embed=CustomEmbed.home())

class CustomEmbed:
    @staticmethod
    def home():
        embed = Embed(
            title="Home",
            description="To be added",
            color=0x6baed6  # Light blue
        )
        embed.set_image(url="https://i.ibb.co/drMxKLP/home.jpg")
        return embed