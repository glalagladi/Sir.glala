import os
import random
import discord
from discord import *
from dotenv import load_dotenv
from variables import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
bot = discord.Bot(command_prefix='?', intents=intents)

# sends a message when the bot is online
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('made by glalagladi'))
    print(f'{bot.user.name} has connected to Discord!')

# this is for loading in all modules :3
if __name__ == "__main__":
    for filename in os.listdir("modules"):
        if filename.endswith(".py"):
            bot.load_extension(f"modules.{filename[:-3]}")

bot.run(TOKEN)

#73 32 108 111 118 101 32 117 32 90 111 101