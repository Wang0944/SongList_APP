from pymongo import MongoClient
import os

class MongoDB:
    _client = None

    @classmethod
    def get_db(cls):
        if not cls._client:
            mongo_user = os.environ.get('MONGO_INITDB_ROOT_USERNAME', 'admin')
            mongo_password = os.environ.get('MONGO_INITDB_ROOT_PASSWORD', 'password')
            mongo_host = os.environ.get('MONGO_HOST', 'localhost')
            mongo_port = int(os.environ.get('MONGO_PORT', 27018))

            uri = f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/"
            cls._client = MongoClient(uri)

        return cls._client["mydatabase"]