import discord
from discord import app_commands, Embed, Interaction
from discord.ext import commands
from discord.ui import Button, Select, View
from embeds import Embeds
import random

# All commands
def setup_commands(bot: commands.Bot):

    # EXPLORE
    @bot.tree.command(name="explore", description="Explore locations.")
    @app_commands.describe(location="Choose a location to explore.")
    @app_commands.choices(location=location_options)
    async def explore(interaction: Interaction, location: app_commands.Choice[str] = None):
        if location:
            if location.value == "market":
                shopkeeper_quote = random.choice(shopkeeper_quotes)
                embed = Embeds.market(shopkeeper_quote)
            elif location.value == "church":
                embed = Embeds.church()
            else:
                embed = Embed(title="Unknown", description="This location does not exist.")

            await interaction.response.send_message(embed=embed)
        else:
            embed = Embeds.explore()
            view = LocationSelect()
            await interaction.response.send_message(embed=embed, view=view)

# =============== DROPDOWNS ===============
class LocationSelect(View):
    def __init__(self):
        super().__init__()
        self.add_item(LocationDropdown())
class LocationDropdown(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Home", description="Craft items, rest your Heroes and take care of your pets.", value="home"),
            discord.SelectOption(label="Church", description="Summon new Heroes.", value="church"),
            discord.SelectOption(label="Market", description="Buy and sell items.", value="market"),
            discord.SelectOption(label="Apothecary", description="Buy and sell potions.", value="apothecary"),
            discord.SelectOption(label="Training Grounds", description="Train your Heroes.", value="traininggrounds"),
            discord.SelectOption(label="Clock Tower", description="Study and work.", value="clocktower"),
            discord.SelectOption(label="Dungeon", description="Explore the Dungeon and fight enemies.", value="dungeon"),
            discord.SelectOption(label="Town Square (Events)", description="Participate in special events.", value="townsquare"),
            discord.SelectOption(label="Hall of Heroes", description="Remember your fallen Heroes.", value="hallofheroes")
        ]
        super().__init__(placeholder="Choose a location", options=options)

    async def callback(self, interaction: Interaction):
        if self.values[0] == "apothecary":
            potionmaster_quote = random.choice(potionmaster_quotes)
            embed = Embeds.apothecary(potionmaster_quote)
        elif self.values[0] == "church":
            embed = Embeds.church()
        elif self.values[0] == "clocktower":
            embed = Embeds.clocktower()
        elif self.values[0] == "dungeon":
            embed = Embeds.dungeon()
        elif self.values[0] == "hallofheroes":
            embed = Embeds.hallofheroes()
        elif self.values[0] == "home":
            embed = Embeds.home()
        elif self.values[0] == "market":
            shopkeeper_quote = random.choice(shopkeeper_quotes)
            embed = Embeds.market(shopkeeper_quote)
        elif self.values[0] == "townsquare":
            embed = Embeds.townsquare()
        elif self.values[0] == "traininggrounds":
            embed = Embeds.traininggrounds()
        else:
            embed = Embed(title="Unknown", description="This location does not exist.")
        await interaction.response.edit_message(embed=embed)

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


location_options = [
    app_commands.Choice(name="Market", value="market"),
    app_commands.Choice(name="Church", value="church")
]