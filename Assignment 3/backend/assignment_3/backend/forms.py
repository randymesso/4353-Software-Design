from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . import models


class RegisterForm(UserCreationForm):
    class Meta:
        model = models.Profile
        fields = ["username", "password"]

class LoginForm(forms.Form):
    username = forms.CharField(label = 'Username', max_length=50)
    password = forms.CharField(label = 'Password', max_length=50)
    class Meta:
        model = models.Profile
        widgets = {
            'password': forms.PasswordInput(),
        }
       
class ProfileManager(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ["fullname", "address1", "address2", "city", "state","zipcode"]