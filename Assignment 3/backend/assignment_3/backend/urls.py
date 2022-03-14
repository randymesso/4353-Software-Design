from django.urls import path
from . import views

# establishes url connection with each html front page 

urlpatterns = [
    path('',views.front_page,name='front_page'),
    path('signup/',views.register.as_view(),name='signup'),
    path('profile_manager',views.profile_manager,name='profile_manager'),
]
