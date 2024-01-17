import requests
from discord.ext import commands
from utils.message import Message


class Kitsu:
    @staticmethod
    async def get_anime(ctx: commands.Context, *search: str):
        base_url = 'https://kitsu.io/api/edge/'
        search_query = ' '.join(search)
        url = f'{base_url}anime?filter[text]={search_query}'

        print(url)

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            animes = data.get('data', [])

            if animes:
                for anime in animes:
                    attributes = anime.get('attributes', {})
                    canonical_title = attributes.get('canonicalTitle', 'N/A')
                    average_rating = attributes.get('averageRating', 'N/A')
                    synopsis = attributes.get('synopsis', 'N/A')
                    poster_image = attributes.get('posterImage', {}).get('original', 'N/A')
                    anime_message = f"Title: {canonical_title} \n Average Rating: {average_rating}\n Synopsis: {synopsis}\n {poster_image}"
                    await Message.reply_message_user(ctx, anime_message)
            else:
                message_error = "No anime"
                await Message.reply_message_user(ctx, message_error)
        else:
            print(f"Error:{response.status_code}")
