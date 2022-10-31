import spotipy
from spotipy.oauth2 import SpotifyOAuth

def main():

    scopes = ["user-library-read", "user-top-read"]

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id="c6f354662a924f81b9af0aa615832c2b",
        client_secret="6127244cbcc64eaa8a20959bb161c7bb",
        redirect_uri="http://localhost", scope=scopes,))

    top_artists = sp.current_user_top_artists(20, 0, "short_term")

    genreDict = {}
    for index, artist in enumerate(top_artists["items"]):
        print(index, artist["genres"])
        for genre in artist["genres"]:
            get_genre_frequency(artist["genres"], genreDict)
    print(genreDict)
    
def get_genre_frequency(genres, genreDict): 
    for genre in genres:
        if genreDict[genre]:
            genreDict[genre] += 1
        else: 
            genreDict[genre] = 1
    return genreDict

main()