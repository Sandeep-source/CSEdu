from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1> franchise home")

def login(request):
    return HttpResponse("<h1> franchise login")

def logout(request):
    return HttpResponse("<h1> franchise logout")

def signup(request):
    return HttpResponse("<h1> franchise signup")
