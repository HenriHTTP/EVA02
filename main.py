###############################################
#           Template made by HenriHTTP        #
#          https://github.com/HenriHTTP       #
#           Copyright© HenriHTTP, 2024        #
###############################################

import disnake
from disnake.ext import commands
import os
import asyncio
from dotenv import load_dotenv


load_dotenv()
DISCORD_TOKEN = os.getenv('TOKEN')
intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)


async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")


asyncio.run(load_cogs())
bot.run(DISCORD_TOKEN)





