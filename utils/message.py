from discord.ext import commands
from views.greetings_view import GreetingView


class Message:
    def __init__(self, ctx: commands.Context, message: str, bot: commands.Bot):
        self.ctx = ctx
        self.message = message
        self.__bot = bot

    @staticmethod
    async def remove_messages(message):
        if "words" in message.content.lower():
            await message.delete()

    async def send_message_user(self):
        try:
            view = GreetingView(self.ctx, self.message, self.__bot)
            message = await self.ctx.send(embed=view.to_embed(), ephemeral=True)
            view.message = message
            return True
        except Exception as error:
            print(error)
            return False

    async def reply_message_user(self):
        try:
            view = GreetingView(self.ctx, self.message, self.__bot)
            message = await self.ctx.reply(embed=view.to_embed())
            view.message = message
            return True
        except Exception as error:
            print(error)
            return False

    async def reply_mention_message(self):
        if self.__bot.user.mentioned_in(self.ctx):
            try:
                view = GreetingView(self.ctx, self.message, self.__bot)
                message = await self.ctx.reply(embed=view.to_embed())
                view.message = message
                return True
            except Exception as error:
                print(error)
                return False
