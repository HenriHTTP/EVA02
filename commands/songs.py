from discord.ext import commands
import discord
from utils.channel import Channel
from utils.message import Message


class Songs(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.__bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        pass

    @commands.command(name="play")
    async def play_song(self, ctx: commands.Context):
        channel = Channel(ctx, self.__bot)
        join_channel = await channel.connect_to_channel()
        member_is_on_voice_channel = join_channel is True
        if member_is_on_voice_channel:
            bot_join_channel = 'bot join on the channel'
            message = Message(ctx, bot_join_channel, self.__bot)
            await message.send_message_user()
            await join_channel
            return
        else:
            error_message = 'you need connected on voice channel for call song commands'
            message = Message(ctx, error_message, self.__bot)
            await message.send_message_user()

    @commands.command(name='stop')
    async def stop_song(self, ctx: commands.Context):
        pass

    @commands.command(name='playlist')
    async def get_playlist(self, ctx: commands.Context):
        pass

    @commands.command(name='skip')
    async def skip_song(self, ctx: commands.Context):
        pass

    @staticmethod
    async def get_song_by_url(url):
        pass


async def setup(bot: commands.Bot):
    await bot.add_cog(Songs(bot))
