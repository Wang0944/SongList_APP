from flask import Flask
from flask_login import LoginManager
from controllers.user_controller import auth_bp
from controllers.song_controller import songs_bp
from models.user import User

app = Flask(__name__)
app.secret_key = 'dev_key'


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'


app.register_blueprint(auth_bp)
app.register_blueprint(songs_bp)

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)

@app.route('/')
def home():
    return "Welcome to the Homepage! Go to /dashboard"

@app.route('/dashboard')
def dashboard():
    return "This is the Dashboard!"

if __name__ == '__main__':
    app.run(debug=True)