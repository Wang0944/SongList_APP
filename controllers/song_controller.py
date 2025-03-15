# We used the flask framework for development
# and all results were returned in the form of Json

from flask import Blueprint, jsonify
from services.deezer_service import DeezerAPI

# Create a Flask blueprint and manage all song-related modules in song_bp
song_bp = Blueprint('song', __name__)

# This method gets all the songs
@song_bp.route('/songs', methods=['GET'])
def get_all_songs():
    songs = DeezerAPI.get_tracks()
    songList = []
    for song in songs:
        songList.append(song.__dict__)

    return jsonify(songList)


# This method is to search by artist name and get the results
@song_bp.route('/songs/search/<artist>')
def search_songs(artist):
    songs = DeezerAPI.get_tracks()
    filtered_songs = []
    for song in songs:
        if artist.lower() in song.name.lower():
            filtered_songs.append(song.__dict__)

    return jsonify(filtered_songs)

