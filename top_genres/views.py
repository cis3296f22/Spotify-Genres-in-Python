from multiprocessing import context
from django import forms
from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Create separate function that returns genre list
# Pass the genre list to any view/template that needs it

# Create your views here.
from django.http import HttpResponse

scopes = ["user-library-read", "user-top-read"]
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="c6f354662a924f81b9af0aa615832c2b",
    client_secret="6127244cbcc64eaa8a20959bb161c7bb",
    redirect_uri="http://localhost", scope=scopes,))

def get_genre_list():
    
      # Increment value in dictionary every time genre is found
    def get_genre_frequency(genres, genreDict):

        for genre in genres:
            if genre in genreDict:
                genreDict[genre] += 1
            else: 
                genreDict[genre] = 1
        return genreDict

    top_artists = sp.current_user_top_artists(20, 0, "short_term")
    
    # Create empty dictionary, put in artists and get frequency of genres from artists 
    genreDict = {}
    for artist in top_artists["items"]:
        get_genre_frequency(artist["genres"], genreDict)
        #for genre in ten genres
        #if genre in artist
        #add artist seed
        for genre in top_ten_genres:
            if genre in artist:
                artist_id = artist["id"]
                 
    # Sort genre count from highest to lowest frequency
    sorted_genres = sorted(genreDict.items(), reverse = True, key=lambda kv:
        (kv[1], kv[0]))
    top_ten_genres = sorted_genres[0:10]
    filtered_top_genres = [x[0] for x in top_ten_genres]
    
    return filtered_top_genres

def login_view(request):
    return render(request, "login.html",{})

def redirect_view(request):
    return render(request, "<h1>Redirect</h1>", {})

def genre_view(request, genres):
    
    genre_list = get_genre_list()
    
    context = {
        "data" : genre_list
    }
      
    return render(request, "genres.html", context)

def generate_playlist_view(request):

#we want the seed to change depending on genre picked. top artist from that genre
    
  
    
    # (recommendations(seed_genres = top_tengenres[user_input_int + 1]))
    genre_recommendations = sp.recommendations(seed_artists=[], limit=20)
    
    new_list = []
    song = ""
    print(sp.recommendation_genre_seeds())
    recommended_list = (genre_recommendations["tracks"])
    for items in recommended_list:
        track_name = items["name"]
        artists = items["artists"]
        for artist in artists:
            artist_name = artist["name"]
        song = track_name + " by " + artist_name
        new_list.append(song)
            
    context = {
        "list" : new_list
    }
    
    return render(request, "playlist_generated.html", context)

def generate_menu_view(request):
    
    return render(request, "generate_menu.html", )

