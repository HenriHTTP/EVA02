import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('TOKEN')
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())


async def load_cogs():
    for packages in os.listdir("./commands"):
        if packages.endswith(".py"):
            await client.load_extension("commands." + packages[:-3])


async def main():
    await load_cogs()
    await client.start(DISCORD_TOKEN)


asyncio.run(main())
