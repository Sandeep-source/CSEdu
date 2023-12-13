from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('login',login),
    path('logout',logout),
    path('signup',signup),
    path('purchase',purchase),
]