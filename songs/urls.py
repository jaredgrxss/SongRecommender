from django.urls import path
from . import views
app_name = 'songs'
urlpatterns = [

    path('spotify/login',views.login,name='spotify-login'),
    path('',views.song_index,name='index'),
    path('random/',views.getRandomSong,name='random'),
]
