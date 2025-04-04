from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from bson import ObjectId
from models.song import Song

songs_bp = Blueprint('songs', __name__)

@songs_bp.route('/dashboard')
@login_required
def dashboard():
    songs = Song.get_by_user(current_user.get_id())
    return render_template('dashboard.html', songs=songs)

@songs_bp.route('/song/add', methods=['GET', 'POST'])
@login_required
def add_song():
    if request.method == 'POST':
        song = Song(
            user_id=current_user.get_id(),
            name=request.form['name'],
            artist=request.form['artist'],
            link=request.form['link'],
            image=request.form['image']
        )
        song.save()
        return redirect(url_for('songs.dashboard'))
    return render_template('add_song.html')

@songs_bp.route('/song/delete/<song_id>')
@login_required
def delete_song(song_id):
    Song.delete(song_id, current_user.get_id())
    return redirect(url_for('songs.dashboard'))