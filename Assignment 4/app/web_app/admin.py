from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm

from .forms import UserCreation, UserChange
from .models import UserCredentials,ClientInformation

class AdminCredentials(UserAdmin):
    add_form = UserCreation
    form = UserChange
    model = UserAdmin
    list_display = ["username","password",]
    
admin.site.register(UserCredentials, UserAdmin)
admin.site.register(ClientInformation)