from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.

def home(request):
    return HttpResponse("<h1> student home")

def login(request):
    return HttpResponse("<h1> student login")

def logout(request):
    return HttpResponse("<h1> student logout")

def signup(request):
    return HttpResponse("<h1> student signup")

def purchase(request):
    return HttpResponse("<h1> Purchase Page")
