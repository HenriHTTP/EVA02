from discord.ext import commands
from utils.message import Message
from services.open_ia import OpenAi


class Gpt(commands.Cog):
    def __init__(self, bot: commands.bot):
        self.__bot = bot

    @commands.command("gpt")
    async def get_message(self, ctx: commands.Context, *message: str):
        message = " ".join(message)
        print(message)
        response = await OpenAi.ask_gpt(message)
        print(response)
        message = Message(ctx, response, self.__bot)
        await message.reply_message_user()


async def setup(bot: commands.bot):
    await bot.add_cog(Gpt(bot))
