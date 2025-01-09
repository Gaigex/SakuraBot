import discord
from discord import Embed
from cogs.utility.register import check_user_registered

def command(bot):
    @bot.tree.command(name="explore", description="Explore locations.")
    async def explore(interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        if not await check_user_registered(user_id, interaction):
            return
        await interaction.response.send_message(embed=CustomEmbed.explore())

class CustomEmbed:
    @staticmethod
    def explore():
        embed = Embed(
            title="Explore",
            description=(
                "- **Home**\n"
                "- **Church**\n"
                "- **Market**\n"
                "- **Apothecary**\n"
                "- **Training Grounds**\n"
                "- **Dungeon**\n"
                "- **Clock Tower**\n"
                "- **Town Square (Events)**\n"
                "- **Hall of Heroes**"
            ),
            color=0x00aeef # Blue
        )
        return embed