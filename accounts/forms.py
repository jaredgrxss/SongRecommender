from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

class MyLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(MyLoginForm, self).__init__(*args, **kwargs)
        self.error_messages['invalid_login']
    
    username = UsernameField(widget=forms.TextInput(
        attrs= {
            'class':'login-user',
            'placeholder':'Enter your username',
            'id':'hello'
            }

    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs = {
            'class':'login-pass',
            'placeholder':'Enter your password',
            'id':'',
        }
    ))


class UserCreateForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username','email','password1','password2') 

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Username"
        self.fields['password1'].label = 'Create Password'
        self.fields['password2'].label = 'Verify Passowrd'

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'login-user',
            'type':'text',
            'placeholder':'username',
        }
    ))
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'',
            'type':'email',
            'placeholder':'email',
        }
    ))
    password1 = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'',
            'type':'password',
            'placeholder':'password',
        }
    ))
    password2 = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'',
            'type':'password',
            'placeholder':'re-enter your password',
        }
    ))
