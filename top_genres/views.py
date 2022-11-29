from multiprocessing import context
from django import forms
from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Create separate function that returns genre list
# Pass the genre list to any view/template that needs it

# Create your views here.
from django.http import HttpResponse

scopes = ["user-library-read", "user-top-read", "playlist-modify-public"]
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="c6f354662a924f81b9af0aa615832c2b",
    client_secret="6127244cbcc64eaa8a20959bb161c7bb",
    redirect_uri="http://localhost", scope=scopes,))

def get_top_artists(term):
    '''Returns a list of the user's top listened-to artists.
    params: term = the time period from which the Spotify API retreives data.'''
    top_artists = sp.current_user_top_artists(50, 0, term)
    return top_artists


def get_artists_of_genre(genre, term):
    '''Returns a list of artists pertaining to the given genre.
    params: genre = the genre to retreive artists from.
            term = the time period from which the Spotify API retreives data.'''
    top_artists = get_top_artists(term)
    artist_of_genre_list = []
    for artist in top_artists["items"]:
        if genre in artist["genres"]:
            artist_of_genre_list.append(artist)
            
    # Returns as a dictionary with several fields. Must be filtered further
    return artist_of_genre_list

                

def get_genre_list(term):
    '''Returns a list of the user's top ten most listened-to genres
    params: genre = the genre to retreive artists from.'''

      # Increment value in dictionary every time genre is found
    def get_genre_frequency(genres, genreDict):

        for genre in genres:
            if genre in genreDict:
                genreDict[genre] += 1
            else: 
                genreDict[genre] = 1
        return genreDict
    
    # Create empty dictionary, put in artists and get frequency of genres from artists 
    genreDict = {}
    
    top_artists = get_top_artists(term)

    for artist in top_artists["items"]:
        get_genre_frequency(artist["genres"], genreDict)
        #for genre in ten genres
        #if genre in artist
        #add artist seed
        '''for genre in top_ten_genres:
            if genre in artist:
                artist_id = artist["id"]'''
                 
    # Sort genre count from highest to lowest frequency
    sorted_genres = sorted(genreDict.items(), reverse = True, key=lambda kv:
        (kv[1], kv[0]))
    top_ten_genres = sorted_genres[0:10]
    filtered_top_genres = [x[0] for x in top_ten_genres]
    
    return filtered_top_genres

# returns a list of songs generated from the provided seeds
def get_generated_playlist(seeds):
    '''Returns a list of songs generated from a given list of artist seeds.
    params: seeds = a list of artist ids used as seeds for the recommendation API function.'''

    
    genre_recommendations = sp.recommendations(seed_artists=seeds, limit=20)
    
    new_list = []
    song = ""
    recommended_list = (genre_recommendations["tracks"])
    for items in recommended_list:
        track_name = items["name"]
        artists = items["artists"]
        for artist in artists:
            artist_name = artist["name"]
        song = track_name + " by " + artist_name
        new_list.append(song)
        
    return recommended_list




#---------------------------
# ----------VIEWS-----------
#---------------------------

def login_view(request):
    '''Returns a login page
    params: request = the HTTP request needed to render the HTML template.'''
    return render(request, "login.html",{})

def genre_view(request):
    '''Returns a page with term and genre radio buttons rendered,
    as well as a button to open the artist selection page.
    params: request = the HTTP request needed to render the HTML template.'''
    context = {}
    term = request.POST.get('term', None)
    genre_list = get_genre_list(term)
    context['data'] = genre_list
    context['terms'] = term
    
    return render(request, "genres.html", context)

def generate_playlist_view(request):
    '''Returns a page with a list of songs and a button
    that adds the songs to a playlist in the user's Spotify library.
    params: request = the HTTP request needed to render the HTML template.'''
    
    context = {}
    
    artist_seeds = []
    artist_dict = {}
    artist_dict['art1'] = request.POST.get('1', None)
    artist_dict['art2'] = request.POST.get('2', None)
    artist_dict['art3'] = request.POST.get('3', None)
    artist_dict['art4'] = request.POST.get('4', None)
    artist_dict['art5'] = request.POST.get('5', None)
    
    for key in artist_dict:
        if artist_dict[key] is not None: 
            artist_seeds.append(artist_dict[key])
            
    artist_list = []
    
    song_list = get_generated_playlist(artist_seeds)
    for items in song_list:
        track_name = items["name"]
        artists = items["artists"]
        for artist in artists:
            artist_name = artist["name"]
        artist_list.append(artist_name)
        

    context['song_list'] = song_list
    context['artist_list'] = artist_list

    return render(request, "playlist_generated.html", context)

def generate_menu_view(request):
    '''Returns a page that renders a list of artists pertaining
    to the genre selected on the previous page.
    params: request = the HTTP request needed to render the HTML template.'''
    context = {}
    genre_index = request.POST.get('genre_index', None)
    term = request.POST.get('term', None)

    genre_list = get_genre_list(term)
    selected_genre = genre_list[int(genre_index)-1]

    unfiltered_artist_list = get_artists_of_genre(selected_genre, term)

    context['term'] = term

    context['artist_list'] = unfiltered_artist_list

    return render(request, "generate_menu.html", context)


def playlist_confirmation_view(request):
    '''Returns a page that adds songs in the previously displayed
    list of songs via http requests. A confirmation message is displayed.
    params: request = the HTTP request needed to render the HTML template.'''
    
    playlist = []
    song_dict = {}
    song_dict['song1'] = request.POST.get('1', None)
    song_dict['song2'] = request.POST.get('2', None)
    song_dict['song3'] = request.POST.get('3', None)
    song_dict['song4'] = request.POST.get('4', None)
    song_dict['song5'] = request.POST.get('5', None)
    song_dict['song6'] = request.POST.get('6', None)
    song_dict['song7'] = request.POST.get('7', None)
    song_dict['song8'] = request.POST.get('8', None)
    song_dict['song9'] = request.POST.get('9', None)
    song_dict['song10'] = request.POST.get('10', None)
    song_dict['song11'] = request.POST.get('11', None)
    song_dict['song12'] = request.POST.get('12', None)
    song_dict['song13'] = request.POST.get('13', None)
    song_dict['song14'] = request.POST.get('14', None)
    song_dict['song15'] = request.POST.get('15', None)
    song_dict['song16'] = request.POST.get('16', None)
    song_dict['song17'] = request.POST.get('17', None)
    song_dict['song18'] = request.POST.get('18', None)
    song_dict['song19'] = request.POST.get('19', None)
    song_dict['song20'] = request.POST.get('20', None)
    
    for key in  song_dict:
        if  song_dict[key] is not None: 
            playlist.append(song_dict[key])
    
    user_id = sp.me()["id"] 
    
    new_playlist = sp.user_playlist_create(user_id, "My Customized Playlist")

    sp.user_playlist_add_tracks(user_id, new_playlist["id"], playlist)
    
    
    return render(request, "playlist_confirmation.html")