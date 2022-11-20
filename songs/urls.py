from django.urls import path
from . import views
app_name = 'songs'
urlpatterns = [

    path('spotify/login',views.login,name='spotify-login'),
    path('',views.song_index,name='index'),
    path('random/',views.getRandomSong,name='random'),
    path('playlist/',views.getPlaylist,name='playlist'),
    path('playsong/',views.playsong,name='playsong'),
    path('stopsong/',views.stopsong,name='stopsong'),
    path('playsong/<track_uri>',views.playPlaylistSong,name='play_playlistsong'),

]
