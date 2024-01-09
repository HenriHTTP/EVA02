import discord
from discord.ext import commands


class Greetings(commands.Cog):
    def __init__(self, bot: commands.bot):
        self.__bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        messages_send_on_server = f'message from  {message.author} content: {message.content}'
        print(messages_send_on_server)

    @commands.Cog.listener()
    async def on_member_join(self, ctx: commands.Context):
        on_member_join_message = f"Welcome to the server, {ctx.author.mention} We're glad to have you here"
        await ctx.author.send(on_member_join_message)

    @commands.command(name='hello')
    async def greet_user(self, ctx: commands.Context):
        greet_user_message = f'hello, {ctx.author} how are you my friend, be welcome to {ctx.guild}'
        await ctx.reply(greet_user_message)


async def setup(bot: commands.bot):
    await bot.add_cog(Greetings(bot))
