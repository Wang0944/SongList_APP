# This class use for connect database
from pymongo import MongoClient


class MongoDB:
    _client = None

    @classmethod
    def get_db(cls):
        if not cls._client:
            cls._client = MongoClient('mongodb://localhost:27017/')
        return cls._client.music_app_db
    # !!!!!!!!Once the database name is determined, remember to change it!!!