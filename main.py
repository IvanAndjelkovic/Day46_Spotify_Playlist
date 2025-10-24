import requests 
from bs4 import BeautifulSoup
import dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth


CLIENT_ID = dotenv.get_key(".env", "CLIENT_ID") 
CLIENT_SECRET = dotenv.get_key(".env", "CLIENT_SECRET")
REDIRECT_URI = "http://localhost:8888/callback"
scope = "playlist-modify-private"


# input_date = input("What Year you would like to travel in format: YYYY-MM-DD:\n")


# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"}

# url = "https://www.billboard.com/charts/hot-100/"+input_date

# response = requests.get(url=url, headers = headers)



# soup = BeautifulSoup(response.text, "html.parser")



# list_100 = []
# tags= soup.select("li.o-chart-results-list__item h3.c-title")
# for tag in tags:
#     song_title = tag.getText().strip()
#     list_100.append(song_title)

# print(list_100)



# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,
#                                                            client_secret=CLIENT_SECRET))

# results = sp.search(q='weezer', limit=20)
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
#     client_id=CLIENT_ID,
#     client_secret=CLIENT_SECRET,
#     redirect_uri=REDIRECT_URI,
#     scope=scope
# ))

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=scope,
    open_browser=True  # This will open the browser automatically
))

# Test the connection
current_user = sp.current_user()
print(f"Connected to Spotify as: {current_user['display_name']}")