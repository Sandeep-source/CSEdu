from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'Scit_FranchiseDashboard.html')

def login(request):
    return render(request,'Scit_Franchies_login.html')

def logout(request):
    return HttpResponse("<h1> franchise logout")

def signup(request):
    return HttpResponse("<h1> franchise signup")
