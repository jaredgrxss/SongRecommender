from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name='homepage'),
    path('songs/',include('songs.urls',namespace='songs')),
    path('accounts/',include('accounts.urls',namespace='accounts'))
]
