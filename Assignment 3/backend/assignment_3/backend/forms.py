from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . import models

class RegisterForm(UserCreationForm):
    class Meta:
        model = models.Profile
        fields = ["username", "password"]

class LoginForm(forms.Form):
    user_name = forms.CharField(label = 'Username', max_length=50)
    password = forms.CharField(label = 'Password', max_length=50)
    class Meta:
        model = models.Profile
        widgets = {
            'password': forms.PasswordInput(),
        }