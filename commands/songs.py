from discord.ext import commands
import discord
from utils.channel import Channel


class Songs(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.__bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        pass

    @commands.command(name="play")
    async def play_song(self, ctx: commands.Context):
        join_channel = Channel.connect_to_channel(ctx)
        if join_channel:
            await ctx.send('bot join on the channel')
            await join_channel
            return
        await ctx.reply('you need connected on voice channel for call song commands')

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

