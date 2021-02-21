from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
load_dotenv()

# Authentication with Spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id = os.getenv('CLIENT_ID'),
        client_secret= os.getenv('CLIENT_SECRET'),
        redirect_uri="http://example.com",
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

date = input("Which year do you want to travel to? Type date in this format YYYY-MM-DD:\n")
billboard_url = "https://www.billboard.com/charts/hot-100/"+date

response = requests.get(billboard_url).text
soup = BeautifulSoup(response,'html.parser')

song_titles = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
song_names = []
for title in song_titles:
    song_names.append(title.getText())

# Search Spotify for the songs
song_uris = []
year = date.split('-')[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = (result['tracks']['items'][0]['uri'])
        song_uris.append(uri)
    except IndexError:
        print(f"{song} Skipped.")

# Adding songs to new playlist
playlist = sp.user_playlist_create(user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)