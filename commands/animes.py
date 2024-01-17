from discord.ext import commands
from discord.ext.commands import bot
from utils.kitsu import Kitsu
from utils.message import Message


class Anime(commands.Cog):
    def __init__(self, bot: commands.bot):
        self.__bot = bot

    @commands.command(name="anime")
    async def search_anime(self, ctx: commands.Context, *search: str):
        await Kitsu.get_anime(ctx,*search)


async def setup(bot: commands):
    await bot.add_cog(Anime(bot))
