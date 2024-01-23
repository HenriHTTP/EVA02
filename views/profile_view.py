###############################################
#           Template made by HenriHTTP        #
#          https://github.com/HenriHTTP       #
#           Copyright© HenriHTTP, 2024        #
###############################################

import disnake
from disnake.ui import View


class ProfileView(View):
    def __init__(self, ctx, title, user_name, user_avatar_url, user_created_at, user_joined_at, user_status):
        super().__init__()
        self.__ctx = ctx
        self.__title = title
        self.__user_name = user_name
        self.__user_avatar_url = user_avatar_url
        self.__user_created_at = user_created_at
        self.__user_joined_at = user_joined_at
        self.__user_status = user_status

    async def interaction_check(self, interaction: disnake.Interaction):
        return interaction.user == self.__ctx.author

    def to_embed(self):
        embed = disnake.Embed(
            title=self.__title,
            description=(
                f"Name: {self.__user_name}\n"
                f"Created At: {self.__user_created_at}\n"
                f"Joined At: {self.__user_joined_at}\n"
                f"Status: {self.__user_status}\n"
            ),
            color=disnake.Color.blue()
        )
        embed.set_thumbnail(url=self.__user_avatar_url)
        return embed
