import discord
import logging

from imdb import IMDb
from discord.ext import commands
from discord.commands import Option, slash_command
from .util.config import Config

log = logging.getLogger(__name__)

"""
features:
    - admin commands
        - delete item
        - force set watched/attendee
        - intial db setup, remove after use
"""

class FratFlicks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config()
        self.imdb = IMDb()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id != 1211852182656126997:
            return
        if message.author.bot:
            return
        # if message.role_mentions has the @movienight role
        # pass to a diff function

    async def post_options(self, message):
        # scan_iter through keys
        # pull list of movies that haven't been watched
        # select 3 random movies from list
        # post with masked links in ordered list
        # 3 reactions for votes
        # another reaction for re-roll
        pass

    async def new_movie(self, message):
        # get imdb link from message
        # pull out id tt01234567
        # use id # with self.imdb.get_movie
        # add via self.config.add()
        # react to the post with check mark
        # add upvote react to track
        # react differently if its a duplicate
        pass

    async def upvote(self, reaction):
        # check the message for the imdb link
        # use self.imdb to get movie title
        # set "upvoted" to list of reactors
        pass

    async def delete_movie(self, message):
        # when user deletes a message
        # remove movie from list unless it was watched
        pass

    @slash_command()
    async def movie(self,
        ctx: discord.ApplicationContext,
        movie_name: Option(str, "Full or Partial name of Movie")
    ):
        """search movies already watched and get info on them"""
        # scan_iter through keys
        # grab all movies matching the name that have been watched
        # create discord ui element to page through items
        # post watched, upvoter, and attendees
        # use movie thumbnail from imdb in embed?

    @slash_command()
    async def watched(self,
        ctx: discord.ApplicationContext,
        imdb_id: Option(str, "id from the URL: tt01234567")
    ):
        """mark a movie as watched, uses imdb id to avoid conflict"""
        # scan_iter through keys
        # grab movie with same imdb_id
        # respond positive and @movienight ask for reactions as attendee
        # add reaction for attendees
        # stop tracking reaction after 2 hours


def setup(bot):
    bot.add_cog(FratFlicks(bot))
