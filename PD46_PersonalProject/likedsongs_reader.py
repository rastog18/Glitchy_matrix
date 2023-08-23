import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import pickle

id = "1b784bebebde447d9dcf0984d01a00da"
secret = "b7dd2994059846f6b46c2dc9739a3331"
song_list = []

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=id,
                                               client_secret=secret,
                                               redirect_uri="http://localhost/",
                                               scope="user-library-read"))


def show_tracks(results):
    for item in results['items']:
        song_list.append(item["track"]["uri"])


results = sp.current_user_saved_tracks()
show_tracks(results)

while results['next']:
    results = sp.next(results)
    show_tracks(results)

file = open("Song_List", "wb")
pickle.dump(song_list, file)
file.close()
