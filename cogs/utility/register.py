import discord
import json

def command(bot):
    @bot.tree.command(name="register", description="Set up your account for the first time.")
    async def register(interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        with open("data/userdata.json", "r") as f:
            userdata = json.load(f)
        if user_id in userdata["masters"]:
            await interaction.response.send_message(
                content="You have already registered!",
                ephemeral=True
                )
            return
        await register_user(user_id, interaction)

# Load user data from the JSON file
def load_user_data():
    with open("data/userdata.json", "r") as f:
        return json.load(f)

# Save user data to the JSON file
def save_user_data(data):
    with open("data/userdata.json", "w") as f:
        json.dump(data, f, indent=4)

# Register user function
async def register_user(user_id, interaction):
    # Load current user data
    userdata = load_user_data()

    # Create a new user data structure
    new_user_data = {
        "inventory": [],
        "heroes": [],
        "command_seals": 0,
        "attributes": { "strength": 0, "magic": 0, "endurance": 0, "luck": 0 },
        "levels": { "level": 1, "exp": 0, "next_level_exp": 100 },
        "last_daily": 0,
        "daily_study": 0,
        "daily_work": 0
    }

    # Add the new user to the data
    userdata["masters"][user_id] = new_user_data

    # Save the updated data back to the file
    save_user_data(userdata)

    # Send a success message to the user
    await interaction.response.send_message(f"Your account has been registered, {interaction.user.name}!", ephemeral=True)

# Checks if user is already registered
async def check_user_registered(user_id, interaction):
    # Load user data from the JSON file
    with open("data/userdata.json", "r") as f:
        userdata = json.load(f)

    # Check if the user_id exists in the "masters" section
    if user_id not in userdata["masters"]:
        # User is not registered
        await interaction.response.send_message(
            "You need to register before doing this action. Use /register to register.",
            ephemeral=True  # Sends the message only to the user
        )
        return False  # Return False indicating the user is not registered
    else:
        return True  # Return True if user is registered