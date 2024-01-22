###############################################
#           Template made by HenriHTTP        #
#          https://github.com/HenriHTTP       #
#           Copyright© HenriHTTP, 2024        #
###############################################

import disnake
from disnake.ui import View


class AnimeView(View):
    def __init__(self, ctx, title, average_rating, synopsis, poster_image):
        super().__init__()
        self.__ctx = ctx
        self.__title = title
        self.__average_rating = average_rating
        self.__synopsis = synopsis
        self.__poster_image = poster_image

    async def interaction_check(self, interaction: disnake.Interaction):
        return interaction.user == self.__ctx.author

    def to_embed(self):
        embed = disnake.Embed(
            title=self.__title,
            description=f"Average Rating: {self.__average_rating}\n Synopsis: {self.__synopsis}",
            color=disnake.Color.blue()
        )
        embed.set_thumbnail(url=self.__poster_image)
        return embed
