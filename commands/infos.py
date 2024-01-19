from discord.ext import commands
from discord.ext.commands import Bot


class Info(commands.Cog):
    def __init__(self, bot: Bot):
        self.__bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.__print_bot_info()

    async def __get_discord_server(self):
        discord_server = [names for names in self.__bot.guilds]
        return discord_server

    async def __get_all_server_count(self):
        return len(self.__bot.guilds)

    async def __get_bot_name(self):
        return self.__bot.user.name

    async def __print_bot_info(self):
        print('###############################################')
        print('#           Template made by HenriHTTP        #')
        print('#          https://github.com/HenriHTTP       #')
        print('#           Copyright© HenriHTTP, 2024        #')
        print('#           Do Not Remove This Header         #')
        print('###############################################\n')
        print(f'message: connected to Discord as Bot{await self.__get_bot_name()}')
        print(f'Message: Bot {await self.__get_bot_name()}connected on {await self.__get_all_server_count()} servers')
        discord_names = await self.__get_discord_server()
        for names in discord_names:
            print('serve:', names)


async def setup(bot: Bot):
    await bot.add_cog(Info(bot))
