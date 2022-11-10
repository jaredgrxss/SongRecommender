from django.shortcuts import render,redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import UserCreateForm,MyLoginForm
# Create your views here.

class SignUp(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name =  'accounts/signup.html' 
