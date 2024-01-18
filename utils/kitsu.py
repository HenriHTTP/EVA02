import requests
from discord.ext import commands
from utils.message import Message
from views.anime_view import AnimeView


class Kitsu:
    def __init__(self, ctx: commands.Context, bot: commands.Bot, *anime: str):
        self.ctx = ctx
        self.__bot = bot
        self.anime = anime

    async def get_anime(self):

        base_url = 'https://kitsu.io/api/edge/'
        search_query = ' '.join(self.anime)
        url = f'{base_url}anime?filter[text]={search_query}'
        response = requests.get(url)
        if response.status_code == 200:
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
                message_error = "No anime"
                message = Message(self.ctx, message_error, self.__bot)
                await message.reply_message_user()
        else:
            print(f"Error:{response.status_code}")

    async def __send_anime_message(self, canonical_title, average_rating, synopsis, poster_image):
        anime_view = AnimeView(
            self.ctx,
            title=canonical_title,
            average_rating=average_rating,
            synopsis=synopsis,
            poster_image=poster_image
        )
        message = await self.ctx.send(embed=anime_view.to_embed(), ephemeral=True)
        anime_view.message = message
