import discord
from discord import Embed
from cogs.utility.register import check_user_registered

def command(bot):
    @bot.tree.command(name="hall_of_heroes", description="Remember your fallen Heroes.")
    async def hall_of_heroes(interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        if not await check_user_registered(user_id, interaction):
            return
        await interaction.response.send_message(embed=CustomEmbed.hall_of_heroes())

class CustomEmbed:
    @staticmethod # Hall of Heroes
    def hall_of_heroes():
        embed = Embed(
            title="Hall of Heroes",
            description="To be added",
            color=0xF8E8C1  # Light yellow
        )
        embed.set_image(url="https://i.ibb.co/6v1d3x3/hall-of-heroes.png")
        return embed