from utils.message import Message
from utils.amazon import Amazon
from discord.ext import commands
from discord.ext.commands import Context, Bot


class Social(commands.Cog):
    def __init__(self, bot: Bot):
        self.__bot = bot

    @commands.command(name='Amazon')
    async def amazon(self, ctx: Context, *search):
        pass


async def setup(bot: Bot):
    await bot.add_cog(Social(bot))
