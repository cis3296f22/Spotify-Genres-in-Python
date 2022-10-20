import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import datetime

import requests


def main():
    now = datetime.datetime.now()
    current_time = datetime.time(now.hour, now.minute)
    if 6 <= now.hour < 12:
        print("Good Morning!")
    elif 12 <= now.hour < 17:
        print("Good Afternoon!")
    elif 17 <= now.hour < 20:
        print("Good Evening!")
    elif 20 <= now.hour < 24 or 0 <= now.hour < 6:
        print("I hope you're having a good night!")
    print(current_time, "seems like a great time to listen to some music!")


    client_credentials_manager = SpotifyClientCredentials(
        client_id='688a719c7b5d4c7783541a026793389f',
        client_secret='c6ce3e951ddd49ca8d9440eaf396deda')
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    mood = input("How are you feeling? ")

    # Each time a mood is selected new playlist is created.
    # The program webscrapes Spotify for the desired playlist.
    # It then extracts the specific fields needed (names and artists) # and saves them as lists.

    if mood == "angry":
        angry_playlist = 'spotify:playlist:7v8D17CS6etGlKEdLl9XzQ'
        angry_songs = sp.user_playlist_tracks('spotify', angry_playlist,
                                              fields='items(track(name))')
        angry_artists = sp.user_playlist_tracks('spotify', angry_playlist,
                                                fields='items(track(artists))')
        print()
        print("Check out these songs...")
        songs = get_songs(angry_songs)
        artists = get_artists(angry_artists)
        finished_playlist = display_songs(songs, artists)
        if not finished_playlist:
            answer = input("Want to try a different playlist? ")
            if validate_diff_playlist():
                mood = "more_angry"
            else:
                print()
                print("Thanks for listening!")

    if mood == "more_angry":
        more_angry_playlist = 'spotify:playlist:0M0nDRHMMeGWH152ZJuRt5'
        more_angry_songs = sp.user_playlist_tracks('spotify',
                                                   more_angry_playlist,
                                                   fields='items(track(name))')
        more_angry_artists = sp.user_playlist_tracks('spotify',
                                                     more_angry_playlist,
                                                     fields='items(track(artists))')
        print()
        print("Check out these songs...")
        songs = get_songs(more_angry_songs)
        artists = get_artists(more_angry_artists)
        display_songs(songs, artists)
        print("Thanks for listening!")

    if mood == "anxious":
        anxious_playlist = 'spotify:playlist:1pBs3D2zFi9sprKOP2dXjy'
        anxious_songs = sp.user_playlist_tracks('spotify', anxious_playlist,
                                                fields='items(track(name))')
        anxious_artists = sp.user_playlist_tracks('spotify', anxious_playlist,
                                                  fields='items(track(artists))')
        print()
        print("Check out these songs...")
        songs = get_songs(anxious_songs)
        artists = get_artists(anxious_artists)
        finished_playlist = display_songs(songs, artists)
        if not finished_playlist:
            if validate_diff_playlist():
                mood = "more_anxious"
            else:
                print()
                print("Thanks for listening!")

    if mood == "more_anxious":
        more_anxious_playlist = 'spotify:playlist:0hFV5PxOBcr1EcpyFZUaoT'
        more_anxious_songs = sp.user_playlist_tracks('spotify',
                                                     more_anxious_playlist,
                                                     fields='items(track(name))')
        more_anxious_artists = sp.user_playlist_tracks('spotify',
                                                       more_anxious_playlist,
                                                       fields='items(track(artists))')
        print()
        print("Check out these songs...")
        songs = get_songs(more_anxious_songs)
        artists = get_artists(more_anxious_artists)
        display_songs(songs, artists)
        print("Thanks for listening!")


    if mood == "calm":
        calm_playlist = 'spotify:playlist:4oZngumZBss8YAloDLoZuq'
        calm_songs = sp.user_playlist_tracks('spotify', calm_playlist,
                                             fields='items(track(name))')
        calm_artists = sp.user_playlist_tracks('spotify', calm_playlist,
                                               fields='items(track(artists))')
        print()
        print("Check out these songs...")
        songs = get_songs(calm_songs)
        artists = get_artists(calm_artists)
        finished_playlist = display_songs(songs, artists)
        if not finished_playlist:
            answer = input("Want to try a different playlist? ")
            if validate_diff_playlist():
                mood = "more_calm"
            else:
                print()
                print("Thanks for listening!")


    if mood == "more_calm":
        more_calm_playlist = 'spotify:playlist:3fXTw38349sEhnNUjuicZy'
        more_calm_songs = sp.user_playlist_tracks('spotify', more_calm_playlist,
                                                  fields='items(track(name))')
        more_calm_artists = sp.user_playlist_tracks('spotify',
                                                    more_calm_playlist,
                                                    fields='items(track(artists))')
        print()
        print("Check out these songs...")
        songs = get_songs(more_calm_songs)
        artists = get_artists(more_calm_artists)
        display_songs(songs, artists)
        print("Thanks for listening!")


    if mood == "excited":
        excited_playlist = 'spotify:playlist:0lz5ePzdGx0PqOIajuRcPe'
        excited_songs = sp.user_playlist_tracks('spotify', excited_playlist,
                                                fields='items(track(name))')
        excited_artists = sp.user_playlist_tracks('spotify', excited_playlist,
                                                  fields='items(track(artists))')
        print()
        print("Check out these songs...")
        songs = get_songs(excited_songs)
        artists = get_artists(excited_artists)
        finished_playlist = display_songs(songs, artists)
        if not finished_playlist:
            if validate_diff_playlist():
                mood = "more_excited"
            else:
                print()
                print("Thanks for listening!")


    if mood == "more_excited":
        more_excited_playlist = 'spotify:playlist:02hy5jkmJVidaxsdILQYZk'
        more_excited_songs = sp.user_playlist_tracks('spotify',
                                                     more_excited_playlist,
                                                     fields='items(track(name))')
        more_excited_artists = sp.user_playlist_tracks('spotify',
                                                       more_excited_playlist,
                                                       fields='items(track(artists))')
        print()
        print("Check out these songs...")
        songs = get_songs(more_excited_songs)
        artists = get_artists(more_excited_artists)
        display_songs(songs, artists)
        print("Thanks for listening!")


    if mood == "happy":
        happy_playlist = 'spotify:playlist:7zewLwuaWUj7XW83IqcQHG'
        happy_songs = sp.user_playlist_tracks('spotify', happy_playlist,
                                              fields='items(track(name))')
        happy_artists = sp.user_playlist_tracks('spotify', happy_playlist,
                                                fields='items(track(artists))')
        print()
        print("Check out these songs...")
        songs = get_songs(happy_songs)
        artists = get_artists(happy_artists)
        finished_playlist = display_songs(songs, artists)
        if not finished_playlist:
            if validate_diff_playlist():
                mood = "more_happy"
            else:
                print()
                print("Thanks for listening!")


    if mood == "more_happy":
        more_happy_playlist = 'spotify:playlist:70mEDFAvnUUHc1G7GRnwxF'
        more_happy_songs = sp.user_playlist_tracks('spotify',
                                                   more_happy_playlist,
                                                   fields='items(track(name))')
        more_happy_artists = sp.user_playlist_tracks('spotify',
                                                     more_happy_playlist,
                                                     fields='items(track(artists))')
        print()
        print("Check out these songs...")
        songs = get_songs(more_happy_songs)
        artists = get_artists(more_happy_artists)
        display_songs(songs, artists)
        print("Thanks for listening!")

    if mood == "heartbroken":

        heartbroken_playlist = 'spotify:playlist:7DLknr2XFAxrhbRhrGUFTe'
        heartbroken_songs = sp.user_playlist_tracks('spotify',
                                                    heartbroken_playlist,
                                                    fields='items(track(name))')
        heartbroken_artists = sp.user_playlist_tracks('spotify',
                                                      heartbroken_playlist,
                                                      fields='items(track(artists))')
        print()
        print("Check out these songs...")
        songs = get_songs(heartbroken_songs)
        artists = get_artists(heartbroken_artists)
        finished_playlist = display_songs(songs, artists)
        if not finished_playlist:
            if validate_diff_playlist():
                mood = "more_heartbroken"
            else:
                print()
                print("Thanks for listening!")


    if mood == "more_heartbroken":
        more_heartbroken_playlist = 'spotify:playlist:0ML495lV8IEp0cxKLg023q'
        more_heartbroken_songs = sp.user_playlist_tracks('spotify',
                                                         more_heartbroken_playlist,
                                                         fields='items(track(name))')
        more_heartbroken_artists = sp.user_playlist_tracks('spotify',
                                                           more_heartbroken_playlist,
                                                           fields='items(track(artists))')
        print()
        print("Check out these songs...")
        songs = get_songs(more_heartbroken_songs)
        artists = get_artists(more_heartbroken_artists)
        display_songs(songs, artists)
        print("Thanks for listening!")


    if mood == "lovey":
        lovey_playlist = 'spotify:playlist:24RFk3tmIifDARS9LjI6a9'
        lovey_songs = sp.user_playlist_tracks('spotify', lovey_playlist,
                                              fields='items(track(name))')
        lovey_artists = sp.user_playlist_tracks('spotify', lovey_playlist,
                                                fields='items(track(artists))')
        print()
        print("Check out these songs...")
        songs = get_songs(lovey_songs)
        artists = get_artists(lovey_artists)
        finished_playlist = display_songs(songs, artists)
        if not finished_playlist:
            if validate_diff_playlist():
                mood = "more_lovey"
            else:
                print()
                print("Thanks for listening!")


    if mood == "more_lovey":
        more_lovey_playlist = 'spotify:playlist:4ASwHUywSR59lMGou7YeQS'
        more_lovey_songs = sp.user_playlist_tracks('spotify',
                                                   more_lovey_playlist,
                                                   fields='items(track(name))')
        more_lovey_artists = sp.user_playlist_tracks('spotify',
                                                     more_lovey_playlist,
                                                     fields='items(track(artists))')
        print()
        print("Check out these songs...")
        songs = get_songs(more_lovey_songs)
        artists = get_artists(more_lovey_artists)
        display_songs(songs, artists)
        print("Thanks for listening!")


    if mood == "nostalgic":

        nostalgic_playlist = 'spotify:playlist:4nY98efG3KdTXhbfl5HnJ1'
        nostalgic_songs = sp.user_playlist_tracks('spotify', nostalgic_playlist,
                                                  fields='items(track(name))')
        nostalgic_artists = sp.user_playlist_tracks('spotify',
                                                    nostalgic_playlist,
                                                    fields='items(track(artists))')
        print()
        print("Check out these songs...")
        songs = get_songs(nostalgic_songs)
        artists = get_artists(nostalgic_artists)
        finished_playlist = display_songs(songs, artists)
        if not finished_playlist:
            if validate_diff_playlist():
                mood = "more_nostalgic"
            else:
                print()
                print("Thanks for listening!")


    if mood == "more_nostalgic":
        more_nostalgic_playlist = 'spotify:playlist:46Ad4tn0f1NGgmffBb52d5'
        more_nostalgic_songs = sp.user_playlist_tracks('spotify',
                                                       more_nostalgic_playlist,
                                                       fields='items(track(name))')
        more_nostalgic_artists = sp.user_playlist_tracks('spotify',
                                                         more_nostalgic_playlist,
                                                         fields='items(track(artists))')
        print()
        print("Check out these songs...")
        songs = get_songs(more_nostalgic_songs)
        artists = get_artists(more_nostalgic_artists)
        display_songs(songs, artists)
        print("Thanks for listening!")


    if mood == "sad":
        sad_playlist = 'spotify:playlist:640ZUrqHYx3UPy8jYZY3uq'
        sad_songs = sp.user_playlist_tracks('spotify', sad_playlist,
                                            fields='items(track(name))')
        sad_artists = sp.user_playlist_tracks('spotify', sad_playlist,
                                              fields='items(track(artists))')
        print()
        print("Check out these songs...")
        songs = get_songs(sad_songs)
        artists = get_artists(sad_artists)
        finished_playlist = display_songs(songs, artists)
        if not finished_playlist:
            if validate_diff_playlist():
                mood = "more_sad"
            else:
                print()
                print("Thanks for listening!")


    if mood == "more_sad":
        more_sad_playlist = 'spotify:playlist:4KdW4oolW3uXZeOQz6EKSy'
        more_sad_songs = sp.user_playlist_tracks('spotify', more_sad_playlist,
                                                 fields='items(track(name))')
        more_sad_artists = sp.user_playlist_tracks('spotify', more_sad_playlist,
                                                   fields='items(track(artists))')
        print()
        print("Check out these songs...")
        songs = get_songs(more_sad_songs)
        artists = get_artists(more_sad_artists)
        display_songs(songs, artists)
        print("Thanks for listening!")


    if mood == "sassy":
        sassy_playlist = 'spotify:playlist:0fQabETAViqlQVVz3rdwT6'
        sassy_songs = sp.user_playlist_tracks('spotify', sassy_playlist,
                                              fields='items(track(name))')
        sassy_artists = sp.user_playlist_tracks('spotify', sassy_playlist,
                                                fields='items(track(artists))')
        print()
        print("Check out these songs...")
        songs = get_songs(sassy_songs)
        artists = get_artists(sassy_artists)
        finished_playlist = display_songs(songs, artists)
        if not finished_playlist:
            if validate_diff_playlist():
                mood = "more_sassy"
            else:
                print()
                print("Thanks for listening!")


    if mood == "more":
        more_sassy_playlist = 'spotify:playlist:05RKjVJVDxAIlWyok1HVaN'
        more_sassy_songs = sp.user_playlist_tracks('spotify',
                                                   more_sassy_playlist,
                                                   fields='items(track(name))')
        more_sassy_artists = sp.user_playlist_tracks('spotify',
                                                     more_sassy_playlist,
                                                     fields='items(track(artists))')
        print()
        print("Check out these songs...")
        songs = get_songs(more_sassy_songs)
        artists = get_artists(more_sassy_artists)
        display_songs(songs, artists)
        print("Thanks for listening!")

# The get_songs(all_hits) function takes [playlist name] = sp.user_playlist_tracks('spotify', [playlist name], fields='items(track(name))') as an argument.
# This argument contains the names of each track in a given playlist.
# Because the track names are contained within several layers of lists and dictionaries, get_songs(all_hits) contains multiple "for" loops to extract the name.
# The function returns a list of strings, with each string being the name of a song within a playlist. Each name is on its own line.

def get_songs(all_hits):
    hits_playlist = []
    for item in all_hits:
        song_list = all_hits.get(item)

    for songs in song_list:
        for name in songs:
            name_list = songs.get(name)
            hits_playlist += name_list.popitem()

    for title in hits_playlist:
        if title == 'name':
            hits_playlist.remove(title)

    final_song_playlist = []
    for item in hits_playlist:
        final_song_playlist.append(item)

    return final_song_playlist

# The get_artists(artists) function takes [playlist name] = sp.user_playlist_tracks('spotify', [playlist name], fields='items(track(artists))') as an argument.
# This argument contains the artists of each track in a given playlist.
# Because the artists are contained within several layers of lists and dictionaries, get_songs(all_hits) contains multiple "for" loops to extract the artists.
# The artist name is contained within a dictionary with other artist info, so the dictionaries were converted to lists, and the artist names were
# located by finding the index of the names.
# The function returns a list of strings, with each string being the name of an artist within a playlist. Each name is on its own line.
def get_artists(artists):
    artist_list = []
    for item in artists:
        temp_artist_list = artists.get(item)

    for artist_sublists in temp_artist_list:
        for items in artist_sublists:
            name_list = artist_sublists.get(items)
            artist_list += name_list.popitem()

    for title in artist_list:
        if title == 'artists':
            artist_list.remove(title)

    final_artist_list = []
    for dictionary_list in artist_list:
        for dictionary in dictionary_list:
            dic_to_list = list(dictionary.values())
            final_artist_list.append(dic_to_list[3])
    return final_artist_list

# display_songs(song_choices, artist_choices) function
# Input: 2 lists song_choices which lists all of the songs in the   # chosen playlist and artist_choices which lists all of artists in # the chosen playlist.
# Processing: The function first finds the amount of songs in the # playlist and then divides it by 4: creating a variable (one,
# two, three, length) for each quarter-point.
# Creates the variable full_playlist which denotes whether the
# full playlist has been displayed to the user and sets it to
# False.
# Prints the song and artist for songs 0-one
# calls ask_again() if True - prints the song and artist for songs # one-two.
# calls ask_again() if True - prints the song and artist for songs # two-three.
# calls ask_again() if True - prints the song and artist for songs # three-length and sets full_playlist = True.
# Output: full_playlist
def display_songs(song_choices, artist_choices):
    length = int(len(song_choices))
    one = int(length / 4)
    two = int(length / 2)
    three = int(3 * length / 4)

    full_playlist = False
    for i in range(one):
        print(song_choices[i], "by", artist_choices[i])
    print()

    if ask_again():
        for i in range(one, two):
            print(song_choices[i], "by", artist_choices[i])
        print()

        if ask_again():
            for i in range(two, three):
                print(song_choices[i], "by", artist_choices[i])
            print()

            if ask_again():
                for i in range(three, length):
                    print(song_choices[i], "by", artist_choices[i])
                    full_playlist = True
                print()
    return full_playlist

# ask_again() function
# Input: none
# Processing: asks the user whether they want more suggestions
# from the playlist they are viewing and validates response.
# Output: True / False
def ask_again():
    answer = input("Want more suggestions from this playlist? ")
    if answer == 'Yes' or answer == 'yes':
        return True
    else:
        return False

# validate_diff_playlist() function
# Input: none
# Processing: asks the user if they want to try a different
# playlist and validates the answer.
# Output: True (Would like different playlist) / False (Would not
def validate_diff_playlist():
    answer = input("Want to try a different playlist? (Y/ N)")
    answer = answer.capitalize()
    while answer != 'Y' and answer != 'N':
        print("Please enter a valid response.")
        answer = input("Want to try a different playlist? (Y / N) ")
        answer = answer.capitalize()


main()

