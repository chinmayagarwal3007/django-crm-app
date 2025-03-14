from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.

def home(request):
    return render(request, 'home.html')

def login_user(request):
    pass

def logout_user(request):
    pass
