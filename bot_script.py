from dotenv import load_dotenv
import os
import discord
from discord.ext import commands

# Load the .env file
load_dotenv()

# Load environment variables
BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("<@107688488509386752> Hello! My name is Rei!")

bot.run(BOT_TOKEN)
