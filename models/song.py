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
    def get_by_id(song_id):
        #Retrieve a song by its ID.
        db = MongoDB.get_db()
        song_data = db.songs.find_one({'_id': ObjectId(song_id)})
        if song_data:
            return Song(
                user_id=song_data.get('createdBy'),
                name=song_data.get('name'),
                artist=song_data.get('artist'),
                link=song_data.get('link'),
                image=song_data.get('image'),
                _id=song_data.get('_id')
            )
        return None

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