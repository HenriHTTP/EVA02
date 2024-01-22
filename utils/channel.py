from utils.message import Message


class Channel:
    def __init__(self, ctx, bot):
        self.__ctx = ctx
        self.__bot = bot

    async def connect_to_channel(self):
        try:
            voice_channel = self.__ctx.author.voice.channel
            if voice_channel:
                await voice_channel.connect()
                return True
        except Exception as error:
            print(f'error: {error}')
            return False
