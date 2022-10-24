import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="c6f354662a924f81b9af0aa615832c2b", 
    client_secret="6127244cbcc64eaa8a20959bb161c7bb", 
    redirect_uri="http://localhost", scope=scope,))

# When running, browser will open a login page to Spotify. Login to Spotify.
# You will be redirected to a localhost URL. Copy this URL and paste it into the
# terminal for this program when prompted.

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
     