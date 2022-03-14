from . import forms
from django.shortcuts import render

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

# No logged in profile pages

# Front page
def front_page(request):
    return render(request, 'front_layout.html', {})

def register(request):
    form = PostForm()

# logged in profile pages    

def profile_manager(request):
    return render(request, 'profile_manager.html',{})

def fuel_history(request):
    return render(request, 'fuel_history.html',{})
    
def fuel_quote(request):
    return render(request, 'fuel_quote_form.html',{})
    
    
# Registration page
class register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    