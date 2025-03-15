from werkzeug.security import generate_password_hash, check_password_hash
#this is need to converse form password to hash. when you need to check password,
# you also need to call check_password_hash to check if it is correct
from flask_login import UserMixin
# Simplifying Flask user management


class User(UserMixin):
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)
        self.playlist = []

    def check_password(self, password):
        return check_password_hash(self.password, password)