# The purpose of this class is to obtain songs on DeezerAPI through the interface
import requests

from models.song import Song


class DeezerAPI:
    BASE_URL = "https://api.deezer.com"

    @classmethod
    def get_tracks(cls):
        response = requests.get(f"{cls.BASE_URL}/chart/0/tracks")
        songList =[]
        for track in response.json()['data']:
            song = Song(
                deezer_id=track['id'],
                title=track['title'],
                artist=track['artist']['name'],
                cover=track['album']['cover_medium'],
                url=track['link']
            )
            songList.append(song)
        return songList




