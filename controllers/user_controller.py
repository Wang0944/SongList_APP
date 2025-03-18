from flask import Blueprint, request, redirect, url_for, flash, render_template
from flask_login import login_user, logout_user
from models.user import User

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User(
            username=request.form['username'],
            email=request.form['email'],
            password=request.form['password']
        )
        user.save()
        return redirect(url_for('auth.login'))
    return render_template('register.html')   #！！！！！前端确定后，需要更改页面地址

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.get_by_username(request.form['username'])
        if user and user.verify_password(request.form['password']):
            login_user(user)
            return redirect(url_for('songs.dashboard'))
        flash('Invalid credentials')
    return render_template('login.html')   #！！！！！！前端确定后，需要更改页面地址

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))