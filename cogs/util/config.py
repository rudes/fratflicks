"""class for managing the Config"""
import logging
import json
import redis

log = logging.getLogger(__name__)

# Schema

"""
"Movie Name": {
    added: "rudes",
    imdb: "tt0000000",
    upvoted: ["rudes", "stickers"],
    watched: {date watched},
    attended: ["rudes", "stickers"]
}
"""

class Config:
    """class for managing the Config"""

    def __init__(self):
        self.db = redis.StrictRedis(host="db")

    def get_movie(self, movie):
        """get a specific value from the config"""
        raw = self.db.get(str(movie))
        return json.loads(raw.decode("utf-8"))

    def get_all(self):
        """get the full config from the db"""
        all_keys = self.db.keys()
        response = []
        for key in all_keys:
            raw = self.db.get(str(key))
            response.append(json.loads(raw.decode("utf-8")))
        return response

    def set(self, movie, setting, value):
        """set a specific value to for a movie"""
        raw = self.db.get(str(movie))
        movie_json = json.loads(raw.decode("utf-8"))
        movie_json[setting] = value
        movie_string = json.dumps(movie_json)
        self.db.set(str(movie), movie_string)

    def add(self, movie, **kwargs):
        """add a new movie to the list"""
        movie_string = json.dumps(kwargs)
        self.db.setnx(str(movie), movie_string)

    def setup_list(self, movies):
        """prepare the database"""
        for movie in movies:
            pass
            # movie is a imdb url
        # pull all messages in 1211852182656126997 thread
        # clean up imdb links
        # store imdb ids in redis db
