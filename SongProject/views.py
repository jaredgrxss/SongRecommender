from django.shortcuts import render,redirect
import spotipy 
from spotipy.oauth2 import SpotifyOAuth
from django.conf import settings 

def homepage(request):
    return render(request,'homepage.html')