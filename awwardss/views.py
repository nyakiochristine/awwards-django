from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
import random
from .forms import PostForm,SignupForm
from .models import Profile,Rating,Post
from django.contrib.auth.models import User


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form= SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            raw_password= form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request, user)
            return redirect('index')
        else:
            form= SignupForm()
        return render(request,'registration/signup.html',{'form':form})
