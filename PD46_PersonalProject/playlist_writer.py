import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import pickle

# These can be accessed from "https://developer.spotify.com/dashboard."
id = "1b784bebebde447d9dcf0984d01a00da"
secret = "b7dd2994059846f6b46c2dc9739a3331"

# Asking for Authorisation
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="1b784bebebde447d9dcf0984d01a00da",
                                               client_secret=secret,
                                               redirect_uri="http://localhost/",
                                               scope="playlist-modify-public"))

# Creating a playlist
user_id = sp.me()['id']
playlist = sp.user_playlist_create(user=user_id, name="Shivam._.Liked", public=True, collaborative=False,
                        description='The follwoing are my liked songs.')
playlist_id = playlist["id"]
print(playlist_id)

#Adding Songs to Playlist
file = open("Song_List","rb")
all_list = pickle.load(file)

start_limit = 0
end_limit = 100
if len(all_list)%100 == 0:
    cycle = len(all_list)/100
else:
    cycle = (len(all_list)//100) + 1

for i in range (0,cycle):
    list_100 = all_list[start_limit:end_limit]
    sp.playlist_add_items(playlist_id=playlist_id, items=list_100, position=None)
    start_limit += 100
    end_limit += 100

# If the endlimit is more than the number of songs no error will pop up.
