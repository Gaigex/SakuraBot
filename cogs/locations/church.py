import discord
from discord import Embed
from cogs.utility.register import check_user_registered

def command(bot):
    @bot.tree.command(name="church", description="Summon new heroes.")
    async def church(interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        if not await check_user_registered(user_id, interaction):
            return
        await interaction.response.send_message(embed=CustomEmbed.church())

class CustomEmbed:
    @staticmethod # Church
    def church():
        embed = Embed(
            title="Church",
            description="To be added",
            color=0xa0a0a0  # Grey
        )
        embed.set_image(url="https://i.ibb.co/5nqQM6P/church.jpg")
        return embed