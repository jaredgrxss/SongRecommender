import requests
from django.shortcuts import render,redirect 
from django.conf import settings
from spotipy import SpotifyOAuth
# Create your views here.

def login(request):
    sp_auth = oauth()
    redirect_url = sp_auth.get_authorize_url()

    return redirect(redirect_url)
    

    


def callback_and_add_song(request):
    pass








def oauth():
    scope = 'user-read-playback-state user-modify-playback-state user-read-currently-playing'
    return SpotifyOAuth(
        scope = scope,
        client_id=settings.CLIENT_ID,
        client_secret=settings.CLIENT_SECRET,
        redirect_uri=settings.REDIRECT_URI,
    )
    



