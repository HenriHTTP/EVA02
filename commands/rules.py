from discord.ext import commands
from utils.message import Message
from discord.ext.commands import Context, Bot


class Rules(commands.Cog):
    def __init__(self, bot: Bot):
        self.__bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx: Context):
        await Message.remove_messages(ctx)
        await self.__reply_to_mention(ctx)

    async def __reply_to_mention(self, ctx: Context):
        try:
            message_reply = f"hello, {ctx.author.name}"
            message = Message(ctx, message_reply, self.__bot)
            await message.reply_mention_message()
        except Exception as error:
            print(error)


async def setup(bot: Bot):
    await bot.add_cog(Rules(bot))
