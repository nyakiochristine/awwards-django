from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Rating,Post,Profile
from django.contrib.auth.models import User


#1signup form for new users

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=300, help_text='Required Input a  valid email address')
    
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
