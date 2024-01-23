###############################################
#           Template made by HenriHTTP        #
#          https://github.com/HenriHTTP       #
#           Copyright© HenriHTTP, 2024        #
###############################################

from utils.message import Message
from disnake.ext import commands
from disnake.ext.commands import Bot


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.__bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        messages_send_on_server = f'message from:  {ctx.author} content: {ctx.content}'
        print(messages_send_on_server)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        on_member_join_message = f"Welcome to the server, {member.name} We're glad to have you here"
        await member.send(on_member_join_message)

    @commands.slash_command(name="hello", description='greetings to user.')
    async def greet_user(self, ctx):
        greet_user_message = f'hello, {ctx.author} how are you my friend, be welcome to {ctx.guild}'
        message = Message(ctx, greet_user_message, self.__bot)
        await message.send_message_user()


def setup(bot):
    bot.add_cog(Greetings(bot))
