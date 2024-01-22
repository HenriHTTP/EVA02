###############################################
#           Template made by HenriHTTP        #
#          https://github.com/HenriHTTP       #
#           Copyright© HenriHTTP, 2024        #
###############################################

from disnake.ext import commands
from disnake.ext.commands import Bot
from services.kitsu import Kitsu


class Anime(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.slash_command(name="anime", description='Search for anime.', auto_defer=True)
    async def search_anime(self, ctx, anime: str = commands.Param()):
        print('comando anime')
        print('Search:', anime)
        if not anime:
            print('no search provided')
            return
        anime = Kitsu(ctx, self.bot, anime)
        await anime.get_anime()
        print(self.bot.user.name)


def setup(bot):
    bot.add_cog(Anime(bot))
