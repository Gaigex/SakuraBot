import discord
from discord import Embed
from cogs.utility.register import check_user_registered

def command(bot):
    @bot.tree.command(name="town_square", description="Participate in special events.")
    async def town_square(interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        if not await check_user_registered(user_id, interaction):
            return
        await interaction.response.send_message(embed=CustomEmbed.town_square())

class CustomEmbed:
    @staticmethod
    def town_square():
        embed = Embed(
            title="Town Square (Events)",
            description="To be added",
            color=0xec008c  # Pink
        )
        return embed