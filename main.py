import requests 
from bs4 import BeautifulSoup
import dotenv
import pprint
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth


CLIENT_ID = dotenv.get_key(".env", "CLIENT_ID") 
CLIENT_SECRET = dotenv.get_key(".env", "CLIENT_SECRET")
REDIRECT_URI = "https://example.com"
scope = "playlist-modify-private"


input_date = input("What Year you would like to travel in format: YYYY-MM-DD:\n")


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"}

url = "https://www.billboard.com/charts/hot-100/"+input_date

response = requests.get(url=url, headers = headers)



soup = BeautifulSoup(response.text, "html.parser")



list_100 = []
tags= soup.select("li.o-chart-results-list__item h3.c-title")
for tag in tags:
    song_title = tag.getText().strip()
    artist = tag.find_next('a').getText().strip()
    list_100.append(f'track: {song_title} artist: {artist} year: {input_date[:4]}')

print(list_100)





# Authenticate and create Spotify object

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=scope,
    open_browser=True  # This will open the browser automatically
))

# Test the connection
current_user = sp.current_user()
print(f"Connected to Spotify as: {current_user['display_name']}")

current_user_id = current_user['id']
# print(f"User ID: {current_user_id}")

# url = sp.search("artist: 'Sam Smith' track: 'Unholy' year: 2022",limit=10,type='track')['tracks']['items'][0]['external_urls']['spotify']
url_list_100 = []
for item in list_100:
    try:
        url = sp.search(item,limit=10,type='track')['tracks']['items'][0]['external_urls']['spotify']
        url_list_100.append(url)
    except IndexError:
        print(f"Song not found on Spotify: {item}")

pprint.pp(url_list_100)
