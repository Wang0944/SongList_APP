from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from bson import ObjectId
from models.song import Song

songs_bp = Blueprint('songs', __name__)

@songs_bp.route('/dashboard')
@login_required
def dashboard():
    songs = Song.get_by_user(current_user.username)
    return render_template('dashboard.html', songs=songs)  #！！！！前段确定后需要改地址

@songs_bp.route('/song/add', methods=['GET', 'POST'])
@login_required
def add_song():
    if request.method == 'POST':
        song = Song(
            user_id=current_user.username,
            title=request.form['title'],
            artist=request.form['artist'],
            image_url=request.form['image_url'],
            song_url=request.form['song_url']
        )
        song.save()
        return redirect(url_for('songs.dashboard'))
    return render_template('song_form.html')   #！！！！前段确定后需要改地址

@songs_bp.route('/song/edit/<song_id>', methods=['GET', 'POST'])
@login_required
def edit_song(song_id):
    if request.method == 'POST':
        updates = {
            'title': request.form['title'],
            'artist': request.form['artist'],
            'image_url': request.form['image_url'],
            'song_url': request.form['song_url']
        }
        Song.update(song_id, updates)
        return redirect(url_for('songs.dashboard'))
    return render_template('song_form.html')   #！！！！前段确定后需要改地址

@songs_bp.route('/song/delete/<song_id>')
@login_required
def delete_song(song_id):
    Song.delete(song_id)
    return redirect(url_for('songs.dashboard'))