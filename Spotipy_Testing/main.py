import spotipy
from spotipy.oauth2 import SpotifyOAuth
#import json


scope = "user-library-read, streaming, user-read-playback-state, user-modify-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="CLIENT_ID_HERE",
                                               client_secret="CLIENT_SECRET_ID_HERE",
                                               redirect_uri="REDIRECT_URI_HERE",
                                               scope=scope))

# a basic driver, does not have error catching
while True:
    playbackData = sp.current_playback()
    # for key in playbackData:
    #     print(key, playbackData[key])
    keyInput = input("Enter control key ")
    if keyInput == 'q':
        print("Quitting")
        break
    elif keyInput == 'k':
        print("Toggle playback")
        if playbackData["is_playing"] is True:
            sp.pause_playback()
        else:
            sp.start_playback()
    elif keyInput == 'l':
        print("Going to next track")
        sp.next_track()
    elif keyInput == 'j':
        print("Going to previous track")
        sp.previous_track()
    elif keyInput == 's':
        print("Toggle shuffle")
        if playbackData["shuffle_state"] is True:
            sp.shuffle(state=False)
        else:
            sp.shuffle(state=True)
    elif keyInput == 'r':
        print("Toggle repeat")
        if playbackData["repeat_state"] is True:
            sp.repeat(state=False)
        else:
            sp.repeat(state=True)
    elif keyInput == 'p':
        songUri = input("Specify song uri: ")
        sp.start_playback(uris=[songUri])
    elif keyInput == 'a':
        albUri = input("Specify album/playlist uri: ")
        sp.start_playback(context_uri=albUri)
    elif keyInput == 'v':
        vol = input("Specify volume % (0-100): ")
        sp.volume(volume_percent=int(vol))
