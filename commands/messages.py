import discord
from discord.ext import commands


class Messages(commands.Cog):
    def __init__(self, bot: commands.bot):
        self.__bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        await self.__remove_messages(message)
        await self.__reply_to_mention(message)

    @staticmethod
    async def __remove_messages(message):
        if "words" in message.content.lower():
            await message.delete()

    async def __reply_to_mention(self, message):
        if self.__bot.user.mentioned_in(message):
            mention_message = f"hello, {message.author.mention}"
            await message.channel.send(mention_message)


async def setup(bot: commands.bot):
    await bot.add_cog(Messages(bot))
