from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

# ------------------------------------ Web Scraping ----------------------------------------#

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, 'html.parser')

all_heading = soup.find_all(name="div", class_="o-chart-results-list-row-container")
song_list = []
singer_list = []

for song in all_heading:
    song_name = song.find(name="h3", id="title-of-a-story").getText().strip()
    song_singer = song.select("li span")[1].getText().strip()
    song_list.append(song_name)
    singer_list.append(song_singer)

# --------------------------------- Spotify URI Searcher ------------------------------------#
# These can be accessed from "https://developer.spotify.com/dashboard."
id = "1b784bebebde447d9dcf0984d01a00da"
secret = "b7dd2994059846f6b46c2dc9739a3331"
uri_list = []
# Asking for Authorisation
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="1b784bebebde447d9dcf0984d01a00da",
                                               client_secret=secret,
                                               redirect_uri="http://localhost/",
                                               scope="playlist-modify-public"))

# There are Multiple songs on Spotify with the same name, hence had to add the artisit's name.
try:
    for i in range(0, len(song_list)):
        uri = sp.search(q=song_list[i] + singer_list[i], type="track")["tracks"]["items"][0]["uri"]
        uri_list.append(uri)
except:
    pass

# --------------------------------- Spotify Playlist Maker ------------------------------------#
playlist = sp.user_playlist_create(user="sr_605", name="SongsBirthdate", public="True",
                                   description="The playlist consists of songs which were on the Hot Billboard on the 25th of January 2005. ")
playlist_id = playlist["id"]

sp.playlist_add_items(playlist_id=playlist_id, items=uri_list, position=None)
