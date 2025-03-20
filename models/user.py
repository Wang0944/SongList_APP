from werkzeug.security import generate_password_hash, check_password_hash
#this is need to converse form password to hash. when you need to check password,
# you also need to call check_password_hash to check if it is correct
from flask_login import UserMixin
# Simplifying Flask user management
from .database import MongoDB
from bson import ObjectId


class User(UserMixin):
    def __init__(self, username, email, password, _id=None):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)
        self._id = _id

    def save(self):
        db = MongoDB.get_db()
        result = db.users.insert_one({
            'name': self.username,  # 改为 'name' 以匹配初始化脚本
            'email': self.email,
            'password': self.password_hash,
            'songs': []
        })
        self._id = result.inserted_id

    @staticmethod
    def get_by_username(username):
        db = MongoDB.get_db()
        user_data = db.users.find_one({'name': username})
        if user_data:
            return User(
                username=user_data['name'],
                email=user_data['email'],
                password=user_data['password'],
                _id=user_data['_id']
            )
        return None

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return str(self._id)

    @staticmethod
    def get_by_id(user_id):
        db = MongoDB.get_db()
        user_data = db.users.find_one({'_id': ObjectId(user_id)})
        if user_data:
            return User(
                username=user_data['name'],
                email=user_data['email'],
                password=user_data['password'],
                _id=user_data['_id']
            )