from utils.message import Message
from utils.amazon import Tiktok
from discord.ext import commands


class Social(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.__bot = bot 
        
    @commands.command(name='Amazon') 
    async def Amazon (self,ctx: commands.Context, *search):
        pass
    
    

async def setup(bot: commands.Bot):
    await bot.add_cog(Social(bot))    