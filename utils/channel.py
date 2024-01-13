from discord.ext import commands


class Channel:

    @staticmethod
    async def connect_to_channel(ctx: commands.Context):
        try:
            voice_channel = ctx.author.voice.channel
            if voice_channel:
                await voice_channel.connect()
                return True
        except Exception as error:
            print(error)
            await ctx.send(f'error: {error}')
            return False
