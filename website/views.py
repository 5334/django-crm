from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    return render(request, 'home.html', {})

#some code was deleted in this line

def logout_user(request):
    pass

  