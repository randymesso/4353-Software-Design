from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UserCredentials,ClientInformation   
       
# form for creating new user        
class UserCreation(UserCreationForm):
    class Meta:
        model = UserCredentials
        fields = ("username",)

# form for changing user credentials
class UserChange(UserChangeForm):
    class Meta:
        model = UserCredentials
        fields = ("username",)

# form for updating/managing client information 
class ProfileManager(forms.ModelForm):
    class Meta:
        model = ClientInformation
        fields = ["fullname", "address1", "address2", "city", "state","zipcode"]