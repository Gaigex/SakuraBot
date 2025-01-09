import discord
from discord import Embed
from cogs.utility.register import check_user_registered

# Command registration function
def command(bot):
    @bot.tree.command(name="apothecary", description="Buy and sell potions.")
    async def apothecary(interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        if not await check_user_registered(user_id, interaction):
            return
        potionmaster_quote = Quote.random_potionmaster()
        await interaction.response.send_message(embed=CustomEmbed.apothecary(potionmaster_quote))

class CustomEmbed:
    @staticmethod
    def apothecary(potionmaster_quote):
        embed = Embed(
            title="Apothecary",
            description="To be added",
            color=0x9a6efc  # Purple
        )
        embed.set_image(url="https://i.ibb.co/LdfVsQY/apothecary.jpg")
        embed.set_footer(
            text=f"{potionmaster_quote}",
            icon_url="https://i.ibb.co/G9Cjj27/potionmaster-portrait.png"
        )
        return embed

class Quote:
    potionmaster = [
        '"Care for a potion? They\'re *purr-fect* for any adventure!"',
        '"Step in, human! My potions are the cat\'s whiskers!"',
        '"Looking for magic? You\'ve come to the right cat!"',
        '"Best potions in town, paws down!"',
        '"Curiosity got you here—leave with a potion!"',
        '"Stock up before your next cat-astrophe!"',
        '"Every sip\'s worth the gold! Care to try one?"',
        '"Don\'t paws! My potions are one of a kind!"',
        '"Meow! What\'ll it be, human? Healing or magic?"',
        '"A potion a day keeps trouble away. Take one!"'
    ]

    @staticmethod
    def random_potionmaster():
        import random
        return random.choice(Quote.potionmaster)