from bson import ObjectId
from .database import MongoDB
class Song:
    def __init__(self,  user_id, title, artist, image_url, song_url):
        self.user_id = user_id
        self.title = title
        self.artist = artist
        self.image_url = image_url
        self.song_url = song_url

    def save(self):
        db = MongoDB.get_db()
        return db.songs.insert_one(self.__dict__).inserted_id

    @staticmethod
    def get_by_user(user_id):
        db = MongoDB.get_db()
        return list(db.songs.find({'user_id': user_id}))

    @staticmethod
    def update(song_id, updates):
        db = MongoDB.get_db()
        db.songs.update_one({'_id': ObjectId(song_id)}, {'$set': updates})

    @staticmethod
    def delete(song_id):
        db = MongoDB.get_db()
        db.songs.delete_one({'_id': ObjectId(song_id)})