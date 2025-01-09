import discord
import json
from discord import Embed
from discord.ui import Button, View
from cogs.utility.register import check_user_registered

# Commands
def command(bot):
    @bot.tree.command(name="delete_account", description="Permanently delete your account and data.")
    async def delete_account(interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        if not await check_user_registered(user_id, interaction):
            await interaction.response.send_message(content="You do not have an account to delete. To create an account, please use /register.", ephemeral=True)
            return
        await interaction.response.send_message(embed=CustomEmbed.delete_confirmation(), view=DeleteConfirmationView(user_id), ephemeral=True)

 # Functions
class DeleteUserData:
    @staticmethod # Function to delete user data
    async def delete(user_id: str):
        # Loads user's data
        with open("data/userdata.json", "r") as f:
            userdata = json.load(f)
        # Deletes user's data
        del userdata["masters"][user_id]
        with open("data/userdata.json", "w") as f:
            json.dump(userdata, f, indent=4)

# Embeds
class CustomEmbed:
    @staticmethod # Confirms user wants to delete account
    def delete_confirmation():
        embed = Embed(
            title="Are you sure you want to delete your account?",
            description="Deleting your account is a permanent action.\nAll of your levels, Heroes, and items will be permanently lost.\nDo you still wish to continue?",
            color=0xFF0000 # Red
        )
        return embed
    @staticmethod # Account deleted
    def delete_account():
        embed = Embed(
            title="Account Deleted",
            description="Your account data has been successfully deleted.\nUse /register to create a new account.",
            color=0xFF0000 # Red
        )
        return embed
    @staticmethod # Canceled deletion
    def cancel_deletion():
        embed = Embed(
            title="Account Deletion Canceled",
            description="Your account deletion has been canceled.\nYou can continue using your account.",
            color=0x00FF00 # Green
        )
        return embed

# Buttons
class DeleteConfirmationView(View):
    def __init__(self, user_id: str):
        self.user_id = user_id
        super().__init__(timeout=60) # Cancels action if user takes > 1 minute to respond

    # Delete button
    @discord.ui.button(label="Delete", style=discord.ButtonStyle.danger, custom_id="delete_account")
    async def delete_button(self, interaction: discord.Interaction, button: Button):
        await DeleteUserData.delete(self.user_id) # Deletes data
        await interaction.response.edit_message(embed=CustomEmbed.delete_account(), view=None)  # Remove buttons after deletion

    # Cancel button
    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.secondary, custom_id="cancel_delete")
    async def cancel_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message(embed=CustomEmbed.cancel_deletion(), ephemeral=True)