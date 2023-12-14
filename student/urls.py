from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('login',login),
    path('logout',logout),
    path('signup',signup),
    path('purchase',purchase),
    path('Scit_Student_forget',forget_password),
    path('verify_certificate',verify_certificate),

]