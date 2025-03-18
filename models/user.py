from werkzeug.security import generate_password_hash, check_password_hash
#this is need to converse form password to hash. when you need to check password,
# you also need to call check_password_hash to check if it is correct
from flask_login import UserMixin
# Simplifying Flask user management
from .database import MongoDB


class User(UserMixin):
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)


    def save(self):
        db = MongoDB.get_db()
        db.users.insert_one({
            'username': self.username,
            'email': self.email,
            'password_hash': self.password_hash
        })

    @staticmethod
    def get_by_username(username):
        db = MongoDB.get_db()
        user_data = db.users.find_one({'username': username})
        if user_data:
            return User(
                username=user_data['username'],
                email=user_data['email'],
                password=user_data['password_hash']
            )
        return None

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)