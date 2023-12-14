from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('Scit_Franchies_login',login),
    path('logout',logout),
    path('signup',signup),
]