import discord
from discord import Embed
from cogs.utility.register import check_user_registered

def command(bot):
    @bot.tree.command(name="training_grounds", description="Train your heroes.")
    async def training_grounds(interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        if not await check_user_registered(user_id, interaction):
            return
        await interaction.response.send_message(embed=CustomEmbed.training_grounds())

class CustomEmbed:
    @staticmethod
    def training_grounds():
        embed = Embed(
            title="Training Grounds",
            description="To be added",
            color=0x5c4033  # Brownish
        )
        embed.set_image(url="https://i.ibb.co/Tgqx4Yv/traininggrounds.jpg")
        return embed