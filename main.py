import os
from dotenv import load_dotenv
from discord import Intents
from discord.ext import commands
import responses  # Import the responses.py file for slash commands

# STEP 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# STEP 1: BOT SETUP
intents = Intents.default()
intents.message_content = True  # NOQA
bot = commands.Bot(command_prefix="!", intents=intents)  # Use commands.Bot for slash commands

# STEP 2: REGISTER SLASH COMMANDS FROM responses.py
responses.setup_commands(bot)  # This will call the function in responses.py to set up the commands

# STEP 3: HANDLING THE STARTUP FOR OUR BOT
@bot.event
async def on_ready():
    print(f'{bot.user} is now running!')

    # Add this to confirm slash command sync
    synced_commands = await bot.tree.sync()
    print(f'Successfully synced {len(synced_commands)} slash commands.')

# STEP 4: MAIN ENTRY POINT
def main():
    bot.run(TOKEN)

if __name__ == '__main__':
    main()
