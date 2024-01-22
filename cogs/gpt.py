###############################################
#           Template made by HenriHTTP        #
#          https://github.com/HenriHTTP       #
#           Copyright© HenriHTTP, 2024        #
###############################################

from disnake.ext import commands
from disnake.ext.commands import Bot
from utils.message import Message
from services.open_ia import OpenAi


class Gpt(commands.Cog):
    def __init__(self, bot: Bot):
        self.__bot = bot

    @commands.slash_command(name="gpt", description="ask something to GPT")
    async def get_message(self, ctx, message: str = commands.Param()):
        print(message)
        response = await OpenAi.ask_gpt(message)
        print(response)
        message = Message(ctx, response, self.__bot)
        await message.reply_message_user()


def setup(bot: Bot):
    bot.add_cog(Gpt(bot))
