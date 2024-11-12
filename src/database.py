from pymongo import MongoClient
from src.utils.singleton import SingletonMeta
import os


class MongoDBConnection(metaclass=SingletonMeta):
    def __init__(self):
        uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
        self._client = MongoClient(uri)
        self._db = self._client['users_db']

    @property
    def db(self):
        return self._db

    def get_collection(self, collection_name):
        return self._db[collection_name]
