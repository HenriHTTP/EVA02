from discord.ext import commands
from services.kitsu import Kitsu
from discord.ext.commands import Bot


class Anime(commands.Cog):
    def __init__(self, bot: Bot):
        self.__bot = bot

    @commands.command(name="anime", description='greetings to user.')
    async def search_anime(self, ctx: commands.Context, *search: str):
        print(*search)
        anime = Kitsu(ctx, self.__bot, *search)
        await anime.get_anime()
        print(self.__bot.user.name)


async def setup(bot: Bot):
    await bot.add_cog(Anime(bot))
