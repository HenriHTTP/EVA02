###############################################
#           Template made by HenriHTTP        #
#          https://github.com/HenriHTTP       #
#           Copyright© HenriHTTP, 2024        #
###############################################

from utils.message import Message
from disnake.ext import commands
from disnake.ext.commands import Bot
import disnake
from views.profile_view import ProfileView


class Profile(commands.Cog):
    def __init__(self, bot):
        self.__bot = bot

    @commands.slash_command(name="profile", description="get infos about a user")
    async def profile(self, ctx, member: disnake.Member = commands.param()):
        user_name = member.name
        user_avatar_url = member.avatar.url if member.avatar else member.default_avatar.url
        user_created_at = member.created_at.strftime("%Y/%m/%d")
        user_joined_at = member.joined_at.strftime("%Y/%m/%d")
        user_status = member.status
        view = ProfileView(
            ctx,
            title="**User Profile**",
            user_name=user_name,
            user_avatar_url=user_avatar_url,
            user_created_at=user_created_at,
            user_joined_at=user_joined_at,
            user_status=user_status,
        )
        embed = view.to_embed()
        message = await ctx.send(embed=embed, ephemeral=True)
        view.message = message


def setup(bot):
    bot.add_cog(Profile(bot))
