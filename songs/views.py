import requests
import random
from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required
from django.conf import settings
from spotipy import SpotifyOAuth
from . import forms 

#USE JSON= for post data
BASE_URL = 'https://api.spotify.com/v1/'
USER_ID = None

############# RANDOM SONG #############
@login_required
def getRandomSong(request):
    #needed_headers
    spheaders = {'Authorization': "Bearer " + request.session['access_token']}
    form = forms.RandomSong(request.POST or None)
    context = {
        'form':form,
    }
    
    if request.method == 'POST':
        if form:
            if form.is_valid():
                gen = form.cleaned_data['genre']

                #url to get songs w a certain genre
                res = requests.get(BASE_URL + 'recommendations?seed_genres=' + gen, headers=spheaders)
                res = res.json()
            
                random_idx = random.randint(0,len(res['tracks']))
                track_uri = res['tracks'][random_idx]['uri']
                request.session['track_uri'] = track_uri
                res = requests.get(BASE_URL + 'tracks/' + res['tracks'][random_idx]['id'], headers=spheaders).json()
                request.session['track_name'] = res['name']
                request.session['artist_name'] = res['artists'][0]['name']

                
                return render(request,'songs/partials/random_song_playable.html')
        else:
            return render(request,'songs/partials/random_song.html',context)

    return render(request,'songs/partials/random_song.html',context)


############### PLAYLIST GENERATOR ###############
@login_required
def getPlaylist(request):
    #get rid of overhead in session variables 
    # gathered from other request
    if 'track_uri' in request.session:
        del request.session['track_uri']

    spheaders = {'Authorization': "Bearer " + request.session['access_token']}
    form = forms.PlaylistGeneratorForm(request.POST or None)
    context = {
        'form':form,
    }

    if request.method == "POST":
        if form:
            if form.is_valid():
                songs = []
                gen1 = form.cleaned_data['genre1']
                gen2 = form.cleaned_data['genre2']
                gen3 = form.cleaned_data['genre3']
                favorite_song = "%20".join(form.cleaned_data['favorite_song'].split(' '))
                search_song = requests.get(BASE_URL + 'search?q=' + favorite_song + "&type=track",headers=spheaders).json()
                search_song = search_song['tracks']['items'][0]['id']
                rec1 =  requests.get(BASE_URL + 'recommendations?seed_genres=' + gen1, headers=spheaders).json()
                rec2 =  requests.get(BASE_URL + 'recommendations?seed_genres=' + gen2, headers=spheaders).json()
                rec3 =  requests.get(BASE_URL + 'recommendations?seed_genres=' + gen3, headers=spheaders).json()
                rec4 = requests.get(BASE_URL + 'recommendations?seed_tracks=' + search_song,headers=spheaders).json()
                for i in range(15):
                    if i < 5:
                        track_uri = rec1['tracks'][i]['uri']
                        song_info = requests.get(BASE_URL + 'tracks/' + rec1['tracks'][i]['id'],headers=spheaders).json()
                        song_name = song_info['name']
                        artist_name = song_info['artists'][0]['name']
                        songs.append((track_uri,song_name,artist_name))
                    elif i < 9:
                        track_uri = rec2['tracks'][i]['uri']
                        song_info = requests.get(BASE_URL + 'tracks/' + rec2['tracks'][i]['id'],headers=spheaders).json()
                        song_name = song_info['name']
                        artist_name = song_info['artists'][0]['name']
                        songs.append((track_uri,song_name,artist_name))
                        
                    elif i < 12:
                        track_uri = rec3['tracks'][i]['uri']
                        song_info = requests.get(BASE_URL + 'tracks/' + rec3['tracks'][i]['id'],headers=spheaders).json()
                        song_name = song_info['name']
                        artist_name = song_info['artists'][0]['name']
                        songs.append((track_uri,song_name,artist_name))
                    else:
                        track_uri = rec4['tracks'][i]['uri']
                        song_info = requests.get(BASE_URL + 'tracks/' + rec4['tracks'][i]['id'],headers=spheaders).json()
                        song_name = song_info['name']
                        artist_name = song_info['artists'][0]['name']
                        songs.append((track_uri,song_name,artist_name))
    

            
                context = {
                    'songs': songs,

                }
                return render(request,'songs/partials/generate_playlist_playable.html',context)  
        else:
            return render(request,'songs/partials/generate_playlist.html',context)


    return render(request,'songs/partials/generate_playlist.html',context)


def playPlaylistSong(request):
    to_play = {"uris":''}


    return render(request,'songs/partials/stop_playlistsong.html')

def stopPlaylistSong(request):



    return render(request,'songs/partials/play_playlist.song.html')


########### PLAYBACK CONTROL RANDOM SONG#############
def playsong(request):
    if 'track_uri' in request.session:
        to_play = {"uris": [request.session['track_uri'] ]}
        spheaders = {'Authorization': "Bearer " + request.session['access_token']}
        requests.put(BASE_URL + 'me/player/play',headers=spheaders,json=to_play)
        del request.session['track_uri']
    else:
        spheaders = {'Authorization': "Bearer " + request.session['access_token']}
        requests.put(BASE_URL + 'me/player/play',headers=spheaders)
        
    return render(request,'songs/partials/stop_song.html')


def stopsong(request):
    spheaders = {'Authorization': "Bearer " + request.session['access_token']}
    requests.put(BASE_URL + 'me/player/pause',headers=spheaders)
    return render(request,'songs/partials/play_song.html')


################ MAIN HOME PAGE #################
@login_required
def song_index(request):
    #needed headers
    spheaders = {'Authorization': "Bearer " + request.session['access_token']}

    #adding username to screen 
    res = requests.get(BASE_URL + 'me/', headers=spheaders).json()
    request.session['user_id'] = res['id']
    request.session['user_name'] = res['display_name'].split(" ")[0]

    return render(request,'songs/init.html')





############### LOGIN AND OAUTH HANDLING ####################
def login(request):
    sp_auth = oauth()
    redirect_url = sp_auth.get_authorize_url()
    token = sp_auth.get_access_token()
    access_token = token['access_token']
    refresh_token = token['refresh_token']
    expires_in = token['expires_in']
    request.session['access_token'] = access_token
    request.session['refresh_token'] = refresh_token
    request.session['expires_in'] = expires_in
    request.session.modified = True
    return redirect(redirect_url)


def oauth():
    scope = 'user-read-playback-state user-modify-playback-state user-read-currently-playing playlist-modify-public playlist-modify-private'
    sp_auth = SpotifyOAuth(
        scope = scope,
        client_id=settings.CLIENT_ID,
        client_secret=settings.CLIENT_SECRET,
        redirect_uri=settings.REDIRECT_URI,
    )
    return sp_auth
    



