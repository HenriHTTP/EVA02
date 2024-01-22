from views.greetings_view import GreetingView
from disnake.ext.commands import Context, Bot


class Message:
    def __init__(self, ctx: Context, message: str, bot: Bot):
        self.__ctx = ctx
        self.__message = message
        self.__bot = bot

    @staticmethod
    async def remove_messages(message):
        if "words" in message.content.lower():
            await message.delete()

    async def send_message_user(self):
        try:
            view = GreetingView(self.__ctx, self.__message, self.__bot)
            embed = view.to_embed()
            message = await self.__ctx.send(embed=embed, ephemeral=True)
            view.__message = message
            return True
        except Exception as error:
            print(error)
            return False

    async def reply_message_user(self):
        try:
            view = GreetingView(self.__ctx, self.__message, self.__bot)
            message = await self.__ctx.reply(embed=view.to_embed())
            view.__message = message
            return True
        except Exception as error:
            print(error)
            return False

    async def reply_mention_message(self):
        if self.__bot.user.mentioned_in(self.__ctx):
            try:
                view = GreetingView(self.__ctx, self.__message, self.__bot)
                message = await self.__ctx.reply(embed=view.to_embed())
                view.__message = message
                return True
            except Exception as error:
                print(error)
                return False
