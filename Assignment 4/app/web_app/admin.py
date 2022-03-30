from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserCredentials

# Register your models here.
admin.site.register(UserCredentials, UserAdmin)