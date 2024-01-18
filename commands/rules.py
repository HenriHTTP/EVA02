from discord.ext import commands
from utils.message import Message


class Rules(commands.Cog):
    def __init__(self, bot: commands.bot):
        self.__bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        await Message.remove_messages(ctx)
        await self.__reply_to_mention(ctx)

    async def __reply_to_mention(self, ctx: commands.Context):
        try:
            message_reply = f"hello, {ctx.author.name}"
            message = Message(ctx, message_reply, self.__bot)
            await message.reply_mention_message()
        except Exception as error:
            print(error)


async def setup(bot: commands.bot):
    await bot.add_cog(Rules(bot))
