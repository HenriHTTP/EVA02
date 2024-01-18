import discord
from discord.ui import View


class AnimeView(View):
    def __init__(self, ctx, title, average_rating, synopsis, poster_image):
        super().__init__()
        self.ctx = ctx
        self.title = title
        self.average_rating = average_rating
        self.synopsis = synopsis
        self.poster_image = poster_image

    async def interaction_check(self, interaction: discord.Interaction):
        return interaction.user == self.ctx.author

    def to_embed(self):
        embed = discord.Embed(
            title=self.title,
            description=f"Average Rating: {self.average_rating}\nSynopsis: {self.synopsis}",
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=self.poster_image)
        return embed
