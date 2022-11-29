from time import sleep
import spotipy
from spotipy.oauth2 import SpotifyOAuth


def main():

    scopes = ["user-library-read", "user-top-read"]

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id="c6f354662a924f81b9af0aa615832c2b",
        client_secret="6127244cbcc64eaa8a20959bb161c7bb",
        redirect_uri="http://localhost", scope=scopes,))

    top_artists = sp.current_user_top_artists(20, 0, "short_term")
    
    # Create empty dictionary, put in artists and get frequency of genres from artists 
    genreDict = {}
    for artist in top_artists["items"]:
        get_genre_frequency(artist["genres"], genreDict)
        
    # Sort genre count from highest to lowest frequency
    sorted_genres = sorted(genreDict.items(), reverse = True, key=lambda kv:
        (kv[1], kv[0]))
    top_ten_genres = sorted_genres[0:10]
    
    # (recommendations(seed_genres = top_tengenres[user_input_int + 1]))
    genre_recommendations = sp.recommendations(seed_genres=['pop'], limit=20)
    
    print(sp.recommendation_genre_seeds())
    recommended_list = (genre_recommendations["tracks"])
    for items in recommended_list:
        track_name = items["name"]
        artists = items["artists"]
        for artist in artists:
            artist_name = artist["name"]
        print(track_name, "by", artist_name)
    
    ''' sorted_dict = {}
    for val in sorted_genres:
       for key in genreDict.keys():
           if genreDict[key] == val:
               sorted_dict[key] = genreDict[key]'''
    
    for index, genre in enumerate(top_ten_genres):
        # Print each genre and its count (sorted)
        result = ', '.join(str(item) for item in genre)
        print(index + 1, result)
        
    
# Increment value in dictionary every time genre is found
def get_genre_frequency(genres, genreDict):
    """top gens

    Args:
        genres (_type_): _description_
        genreDict (_type_): _description_

    Returns:
        _type_: _description_
    """    

    for genre in genres:
        if genre in genreDict:
            genreDict[genre] += 1
        else: 
            genreDict[genre] = 1
    return genreDict

main()
