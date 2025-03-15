from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, login_required
from models.user import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    new_user = User(
        email=data['email'],
        username=data['username'],
        password=data['password']
    )
 # The functions of saving registered users and logging in need to be completed by the db module.