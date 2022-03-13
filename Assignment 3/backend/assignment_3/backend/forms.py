from django import forms

from . import models

class LoginForm(forms.Form):
    user_name = forms.CharField(label = 'Username', max_length=50)
    password = forms.CharField(label = 'Password', max_length=50)
    class Meta:
        model = models.Profile
        widgets = {
            'password': forms.PasswordInput(),
        }