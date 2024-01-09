from discord.ext import commands


class Message:
    @staticmethod
    async def reply_message_user(ctx: commands.Context, message: str):
        try:
            await ctx.reply(message)
        except Exception as error:
            print(error)
            return False

    @staticmethod
    async def send_message_user(ctx: commands.Context, message: str):
        try:
            await ctx.send(message)
        except Exception as error:
            print(error)
            return False

    @staticmethod
    async def remove_messages(message):
        if "words" in message.content.lower():
            await message.delete()

    @staticmethod
    async def reply_mention_message(bot: commands.Bot, ctx: any, message: str):
        if bot.user.mentioned_in(ctx):
            mention_message = message
            try:
                await ctx.channel.send(mention_message)
                return True
            except Exception as error:
                print(error)
                return False
