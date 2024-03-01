"""fratflicks class"""
import logging
import discord

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
    """Handlers and Commands for bot"""
    def __init__(self, bot):
        self.bot = bot
        self.imdb = IMDb()
        self.config = Config()

    @commands.Cog.listener()
    async def on_message(self, message):
        """handle certain messages sent in the discord"""
        try:
            if message.channel.id != 1211852182656126997:
                return
            if message.author.bot:
                return
            movie_role = message.guild.get_role(1213246322405150772)
            if movie_role in message.role_mentions:
                await self.post_options(message)
            if 'imdb' in message.contents.lower():
                await self.new_movie(message)
        except Exception as e: # pylint: disable=W0718
            log.exception(f'on_message,{type(e)} error occured, {e}') #pylint: disable=W1203

    async def post_options(self, message):
        """post options for people to choose from"""
        # scan_iter through keys
        # pull list of movies that haven't been watched
        # select 3 random movies from list
        # post with masked links in ordered list
        # 3 reactions for votes
        # another reaction for re-roll

    async def new_movie(self, message):
        """handle adding a movie from a imdb link to the db"""
        # get imdb link from message
        # pull out id tt01234567
        # use id # with self.imdb.get_movie
        # add via self.config.add()
        # react to the post with check mark
        # add upvote react to track
        # react differently if its a duplicate

    async def upvote(self, reaction):
        """save upvoters to a movie"""
        # check the message for the imdb link
        # use self.imdb to get movie title
        # set "upvoted" to list of reactors

    async def delete_movie(self, message):
        """remove a movie from the db when the message is deleted"""
        # when user deletes a message
        # remove movie from list unless it was watched

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
    """load bot"""
    bot.add_cog(FratFlicks(bot))
