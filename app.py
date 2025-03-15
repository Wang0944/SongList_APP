from flask import Flask
from controllers import song_controller, user_controller, playlist_controller

app = Flask(__name__)


app.register_blueprint(song_controller.song_bp)
app.register_blueprint(user_controller.user_bp)
app.register_blueprint(playlist_controller.playlist_bp)