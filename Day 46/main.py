from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# spotify credentails
CLIENT_ID = "d946ad2c024d420da3556aea0b763ecf"
CLIENT_SECRET = "1294bfa3e0664e58b85ac21f77ab37eb"
REDIRECT_URI = "http://localhost:8888" 
SCOPE ="playlist-modify-private playlist-modify-public"
# SCOPE = "user-library-read user-modify-playback-state"

URL ="https://www.billboard.com/charts/hot-100/#"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

# top_songs = soup.find_all(name="h3", id="title-of-a-story")
top_songs= soup.select("li ul li h3")
song_title =[song.getText().strip() for song in top_songs]
print(song_title)


# Authenticate and get user access token
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI, scope=SCOPE, show_dialog=True,
                                                cache_path="token.txt", requests_timeout=30))

# Fetch the current user's saved tracks
results = sp.current_user_saved_tracks()
for item in results["items"]:
    track = item["track"]
    print(f"{track['name']} by {track['artists'][0]['name']}")

# print(sp.me())  # Fetch current user info

user_id = sp.current_user()["id"]
song_uris = []
year = date.split("-")[0]
for song in song_title:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist["id"], tracks=song_uris)

result = sp.search(q="track:Shape of You year:2017", type="track")
print(result)