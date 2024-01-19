import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv


load_dotenv()
DISCORD_TOKEN = os.getenv('TOKEN')
client = commands.Bot(command_prefix="/", intents=discord.Intents.all())


async def load_cogs():
    for packages in os.listdir("./commands"):
        if packages.endswith(".py"):
            await client.load_extension("commands." + packages[:-3])


asyncio.run(load_cogs())
client.run(DISCORD_TOKEN)
