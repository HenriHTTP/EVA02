from discord.ext import commands
from discord.ext.commands import bot
from utils.kitsu import Kitsu
from utils.message import Message
from discord.ui import Button, view


class Anime(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.__bot = bot

    @commands.command(name="anime")
    async def search_anime(self, ctx: commands.Context, *search: str):
        print(*search)
        anime = Kitsu(ctx, self.__bot, *search)
        await anime.get_anime()
        print(self.__bot.user.name)


async def setup(bot: commands.Bot):
    await bot.add_cog(Anime(bot))
