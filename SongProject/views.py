from django.shortcuts import render,redirect
import spotipy 
from spotipy.oauth2 import SpotifyOAuth
from django.conf import settings 

def homepage(request):
    context = {
        
    }
    return render(request,'homepage.html',context)