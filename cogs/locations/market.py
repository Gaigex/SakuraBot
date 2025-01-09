import discord
from discord import Embed
from cogs.utility.register import check_user_registered

def command(bot):
    @bot.tree.command(name="market", description="Buy and sell items.")
    async def market(interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        if not await check_user_registered(user_id, interaction):
            return
        shopkeeper_quote = Quote.random_shopkeeper()
        await interaction.response.send_message(embed=CustomEmbed.market(shopkeeper_quote))

class CustomEmbed:
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

class Quote:
    shopkeeper = [
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

    @staticmethod
    def random_shopkeeper():
        import random
        return random.choice(Quote.shopkeeper)