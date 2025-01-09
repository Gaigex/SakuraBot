import discord
from ..cogs.locations.apothecary import command as apothecary
from ..cogs.locations.church import command as church
from ..cogs.locations.clock_tower import command as clock_tower
from ..cogs.locations.dungeon import command as dungeon
from ..cogs.locations.hall_of_heroes import command as hall_of_heroes
from ..cogs.locations.home import command as home
from ..cogs.locations.market import command as market
from ..cogs.locations.town_square import command as town_square
from ..cogs.locations.training_grounds import command as training_grounds
from ..cogs.utility.daily import command as daily
from ..cogs.utility.explore import command as explore
from ..cogs.utility.register import command as register
from ..cogs.utility.delete_account import command as delete_account

def setup_commands(bot: discord.ext.cogs.Bot):
    apothecary(bot)
    church(bot)
    clock_tower(bot)
    dungeon(bot)
    hall_of_heroes(bot)
    home(bot)
    market(bot)
    town_square(bot)
    training_grounds(bot)
    daily(bot)
    explore(bot)
    register(bot)
    delete_account(bot)