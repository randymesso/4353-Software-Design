from . import forms
from django.shortcuts import render

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

# No logged in profile pages

# Front page
def front_page(request):
    return render(request, 'front_layout.html', {})

# Login page
def login(request):
    return render(request, 'login.html', {})

# Registration page
def register(request):
    return render(request, 'register.html',{})

# logged in profile pages    

def profile_manager(request):
    return render(request, 'profile_manager.html',{})

def fuel_history(request):
    return render(request, 'fuel_history.html',{})
    
def fuel_quote(request):
    return render(request, 'fuel_quote_form.html',{})