from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . import models
       
class ProfileManager(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ["fullname", "address1", "address2", "city", "state","zipcode"]