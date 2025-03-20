from bson import ObjectId
from .database import MongoDB
class Song:
    def __init__(self, user_id, name, artist, link, image, _id=None):
        self.user_id = user_id
        self.name = name
        self.artist = artist
        self.link = link
        self.image = image
        self._id = _id

    def save(self):
        db = MongoDB.get_db()
        result = db.songs.insert_one({
            'name': self.name,
            'artist': self.artist,
            'link': self.link,
            'image': self.image,
            'createdBy': ObjectId(self.user_id)
        })
        self._id = result.inserted_id
        # update songs list
        db.users.update_one(
            {'_id': ObjectId(self.user_id)},
            {'$push': {'songs': self._id}}
        )

    @staticmethod
    def get_by_user(user_id):
        db = MongoDB.get_db()
        return list(db.songs.find({'createdBy': ObjectId(user_id)}))

    @staticmethod
    def update(song_id, updates):
        db = MongoDB.get_db()
        db.songs.update_one({'_id': ObjectId(song_id)}, {'$set': updates})

    @staticmethod
    def delete(song_id, user_id):
        db = MongoDB.get_db()
        db.songs.delete_one({'_id': ObjectId(song_id)})
        # delete songs from this user
        db.users.update_one(
            {'_id': ObjectId(user_id)},
            {'$pull': {'songs': ObjectId(song_id)}}
        )