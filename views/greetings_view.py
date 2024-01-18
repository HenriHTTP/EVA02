import discord
from discord.ui import View
from discord.ext import commands


class GreetingView(View):
    def __init__(self, ctx: commands.Context, message: str, bot: commands.Bot):
        super().__init__()
        self.ctx = ctx
        self.message = message
        self.bot = bot

    async def interaction_check(self, interaction: discord.Interaction):
        return interaction.user == self.ctx.author

    def to_embed(self):
        embed = discord.Embed(
            title=self.bot.user.name,
            description=f"{self.message}",
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        return embed
