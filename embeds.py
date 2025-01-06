import discord
from discord import Embed
import random

class Embeds:
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
            color=0x00aeef  # Blue
        )
        embed.set_footer(text="You can also use /explore [location] to go straight to a location!")
        return embed

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

    @staticmethod
    def church():
        embed = Embed(
            title="Church",
            description="To be added",
            color=0xa0a0a0  # Grey
        )
        embed.set_image(url="https://i.ibb.co/5nqQM6P/church.jpg")
        return embed

    @staticmethod
    def clocktower():
        embed = Embed(
            title="Clock Tower",
            description="To be added",
            color=0xFFD700  # Yellow
        )
        embed.set_image(url="https://i.ibb.co/MgxW2bb/clocktower.jpg")
        return embed

    @staticmethod
    def dungeon():
        embed = Embed(
            title="Dungeon",
            description="To be added",
            color=0x1a3a66  # Dark blue
        )
        embed.set_image(url="https://i.ibb.co/MBQG84S/dungeon.jpg")
        return embed

    @staticmethod
    def hallofheroes():
        embed = Embed(
            title="Hall of Heroes",
            description="To be added",
            color=0xF8E8C1  # Light yellow
        )
        embed.set_image(url="https://i.ibb.co/6v1d3x3/hall-of-heroes.png")
        return embed

    @staticmethod
    def home():
        embed = Embed(
            title="Home",
            description="To be added",
            color=0x6baed6  # Light blue
        )
        embed.set_image(url="https://i.ibb.co/drMxKLP/home.jpg")
        return embed

    @staticmethod
    def market(shopkeeper_quote):
        embed = Embed(
            title="Market",
            description="Buy and sell items at the market!",
            color=0xcc3429  # Red
        )
        embed.set_image(url="https://i.ibb.co/jLjZd0Z/market.jpg")
        embed.set_footer(
            text=f"{shopkeeper_quote}",
            icon_url="https://i.ibb.co/xsVnckt/shopkeeper-portrait.png"
        )
        return embed

    @staticmethod
    def townsquare():
        embed = Embed(
            title="Town Square (Events)",
            description="To be added",
            color=0xec008c  # Pink
        )
        return embed

    @staticmethod
    def traininggrounds():
        embed = Embed(
            title="Training Grounds",
            description="To be added",
            color=0x5c4033  # Brownish
        )
        embed.set_image(url="https://i.ibb.co/Tgqx4Yv/traininggrounds.jpg")
        return embed


# =============== QUOTES ===============
shopkeeper_quotes = [
    '"Welcome to the Market! What are you in the mood to buy today?"',
    '"Ah, a customer! Can I interest you in some fine wares?"',
    '"Step right up! The finest items in all the land are here!"',
    '"Looking for something special? I\'ve got just the thing for you."',
    '"Only the best for Masters like you! What can I get for you today?"',
    '"Ah, a fellow Master! Care to see what I have on offer?"',
    '"A wise Master knows when to shop! How can I help you today?"',
    '"A little shopping never hurt anyone, right? What can I get for you?"',
    '"Is there anything you desire? I\'ve got plenty to offer!"'
]
potionmaster_quotes = [
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