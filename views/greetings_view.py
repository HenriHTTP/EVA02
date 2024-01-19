import discord
from discord.ui import View
from discord.ext import commands


class GreetingView(View):
    def __init__(self, ctx: commands.Context, message: str, bot: commands.Bot):
        super().__init__()
        self.__ctx = ctx
        self.__message = message
        self.__bot = bot

    async def interaction_check(self, interaction: discord.Interaction):
        return interaction.user == self.__ctx.author

    def to_embed(self):
        embed = discord.Embed(
            title=self.__bot.user.name,
            description=f"{self.__message}",
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=self.__bot.user.avatar.url)
        return embed
