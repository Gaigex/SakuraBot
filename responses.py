import discord
from discord import app_commands, Embed, Interaction
from discord.ext import commands
from discord.ui import Button, Select, View
from embeds import Embeds, Quotes
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
                shopkeeper_quote = Quotes.random_shopkeeper()
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
    
    # HELLO - TEST COMMAND
    @bot.tree.command(name="hello", description="Say hello!")
    async def hello(interaction: discord.Interaction):
        await interaction.response.send_message("Hello there!")

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
            potionmaster_quote = Quotes.random_potionmaster()
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
            shopkeeper_quote = Quotes.random_shopkeeper()
            embed = Embeds.market(shopkeeper_quote)
        elif self.values[0] == "townsquare":
            embed = Embeds.townsquare()
        elif self.values[0] == "traininggrounds":
            embed = Embeds.traininggrounds()
        else:
            embed = Embed(title="Unknown", description="This location does not exist.")
        await interaction.response.edit_message(embed=embed)

location_options = [
    app_commands.Choice(name="Market", value="market"),
    app_commands.Choice(name="Church", value="church")
]