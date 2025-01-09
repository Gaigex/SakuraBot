import discord
from discord import Embed
from cogs.utility.register import check_user_registered

def command(bot):
    @bot.tree.command(name="dungeon", description="Explore the dungeon and fight enemies.")
    async def dungeon(interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        if not await check_user_registered(user_id, interaction):
            return
        await interaction.response.send_message(embed=CustomEmbed.dungeon())

class CustomEmbed:
    @staticmethod # Dungeon
    def dungeon():
        embed = Embed(
            title="Dungeon",
            description="To be added",
            color=0x1a3a66  # Dark blue
        )
        embed.set_image(url="https://i.ibb.co/MBQG84S/dungeon.jpg")
        return embed