from django.urls import path

from . import views

# establishes url connection with each html front page 

urlpatterns = [
    path('',views.front_page,name='front_page'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('profile_manager',views.register,name='profile_manager'),
    path('fuel_history',views.register,name='fuel_history'),
    path('fuel_quote',views.register,name='fuel_quote')
]