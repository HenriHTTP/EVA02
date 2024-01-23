###############################################
#           Template made by HenriHTTP        #
#          https://github.com/HenriHTTP       #
#           Copyright© HenriHTTP, 2024        #
###############################################

from disnake.ext import commands
from utils.message import Message
from disnake.ext.commands import Context, Bot


class Rules(commands.Cog):
    def __init__(self, bot: Bot):
        self.__bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx: Context):
        await Message.remove_messages(ctx)
        await self.__reply_to_mention(ctx)

    @commands.slash_command(name='rules', description="rules server")
    async def rules_server(self, ctx):
        rules = (
            "Rules server\n"
            "1. Lorem ipsum dolor sit amet\n"
            "2. Consectetur adipiscing elit\n"
            "3. Sed do eiusmod tempor incididunt\n"
            "4. Ut labore et dolore magna aliqua\n"
            "5. Ut enim ad minim veniam"
        )
        message = Message(ctx, rules, self.__bot)
        await message.send_message_user()

    async def __reply_to_mention(self, ctx: Context):
        try:
            message_reply = f"hello, {ctx.author.name}"
            message = Message(ctx, message_reply, self.__bot)
            await message.reply_mention_message()
        except Exception as error:
            print(error)


def setup(bot: Bot):
    bot.add_cog(Rules(bot))
