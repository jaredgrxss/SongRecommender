from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from . import forms

app_name = 'accounts'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html',authentication_form=forms.MyLoginForm),name='login'),
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
]
