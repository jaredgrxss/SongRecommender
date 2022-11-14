from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth import get_user_model

class MyLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(MyLoginForm, self).__init__(*args, **kwargs)
        self.error_messages['invalid_login']
        self.fields['username'].label = ''
        self.fields['password'].label = ''


    username = UsernameField(widget=forms.TextInput(
        attrs= {
            'class':'input-fields',
            'placeholder':'Enter Your Username',
            'id':'hello'
            }

    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs = {
            'class':'input-fields',
            'placeholder':'Enter Your Password',
            'id':'',
        }
    ))


class UserCreateForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username','email','password1','password2') 

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].label = ""
        self.fields['email'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'input-fields',
            'type':'text',
            'placeholder':'Username',
        }
    ))
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'input-fields',
            'type':'email',
            'placeholder':'Email',
        }
    ))
    password1 = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'input-fields',
            'type':'password',
            'placeholder':'Password',
        }
    ))
    password2 = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'input-fields',
            'type':'password',
            'placeholder':'Re-enter Your Password',
        }
    ))
