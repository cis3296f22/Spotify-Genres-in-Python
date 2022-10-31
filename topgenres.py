import spotipy
from spotipy.oauth2 import SpotifyOAuth


scopes = ["user-library-read", "user-top-read"]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="c6f354662a924f81b9af0aa615832c2b",
    client_secret="6127244cbcc64eaa8a20959bb161c7bb",
    redirect_uri="http://localhost", scope=scopes,))

top_artists = sp.current_user_top_artists(20, 0, "short_term")

for index, artist in enumerate(top_artists["items"]):
    print(index, artist["name"])