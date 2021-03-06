from django.urls import path
from . import views

urlpatterns = [
    path('',views.front_page,name='front_page'),
    path('signup/',views.register.as_view(),name='signup'),
    path('profile_manager',views.profile_manager,name='profile_manager'),
    path('fuel_quote',views.fuel_quote,name='fuel_quote'),
    path('fuel_history',views.fuel_history,name='fuel_history'),
]
