import requests
from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required
from django.conf import settings
from spotipy import SpotifyOAuth
from . import forms 
# Create your views here.

@login_required
def getRandomSong(request):
    form = forms.RandomSong(request.POST or None)
    context = {
        'form':form,
    }

    return render(request,'songs/partials/random_song.html',context)


@login_required
def song_index(request):
    return render(request,'songs/init.html')


def login(request):
    sp_auth = oauth()
    redirect_url = sp_auth.get_authorize_url()
    code = request.GET.get('code','')
    token = sp_auth.get_access_token(code=code)
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
    



