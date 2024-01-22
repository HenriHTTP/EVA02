###############################################
#           Template made by HenriHTTP        #
#          https://github.com/HenriHTTP       #
#           Copyright© HenriHTTP, 2024        #
###############################################

import requests
from views.anime_view import AnimeView


class Kitsu:
    def __init__(self, ctx, bot, anime: str):
        self.__ctx = ctx
        self.__bot = bot
        self.__anime = anime

    async def get_anime(self):
        print(self.__anime)
        await self.__no_anime()
        base_url = 'https://kitsu.io/api/edge/'
        url_search = f'{base_url}anime?filter[text]={self.__anime}'
        response = requests.get(url_search)
        response_is_complete = response.status_code == 200
        try:
            if response_is_complete:
                data = response.json()
                animes = data.get('data', [])
                if response:
                    for anime in animes:
                        attributes = anime.get('attributes', {})
                        canonical_title = attributes.get('canonicalTitle', 'N/A')
                        average_rating = attributes.get('averageRating', 'N/A')
                        synopsis = attributes.get('synopsis', 'N/A')
                        poster_image = attributes.get('posterImage', {}).get('original', 'N/A')
                        await self.__send_anime_message(canonical_title, average_rating, synopsis, poster_image)
                else:
                    await self.__ctx.send('No anime found')
        except Exception as error:
            print(error)
        else:
            print(f"Request Error:{response.status_code}")

    async def __send_anime_message(self, canonical_title, average_rating, synopsis, poster_image):
        anime_view = AnimeView(
            self.__ctx,
            title=canonical_title,
            average_rating=average_rating,
            synopsis=synopsis,
            poster_image=poster_image
        )
        embed = anime_view.to_embed()
        message = await self.__ctx.send(embed=embed, ephemeral=True)
        anime_view.message = message

    async def __no_anime(self):
        if not self.__anime:
            await self.__ctx.send("No anime")
            return False
