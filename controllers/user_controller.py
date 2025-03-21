from flask import Blueprint, request, redirect, url_for, flash, render_template
from flask_login import login_user, logout_user, login_required
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
    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        print(f"Received login attempt: username={username}")  # Debugging

        user = User.get_by_username(username)
        print(f"User found in DB: {user}")  # Check if user exists

        if user and user.verify_password(password):
            print("Password verified successfully!")
            login_user(user)
            print(f"Login successful! Redirecting to {url_for('songs.dashboard')}")
            return redirect(url_for('songs.dashboard'))
        else:
            print("Login failed! Invalid credentials.")

        flash("Invalid username or password", "danger")
    
    return render_template('login.html')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))