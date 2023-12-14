from django.shortcuts import render
from .forms import FranciseForm

def index(request):
    form = FranciseForm(request.POST or None)
    return render(request,"index.html",context={"form":form})

def home(request):
    return render(request,"index.html")

def home_dark(request):
    return render(request,"it_home_dark.html")

def about(request):
    return render(request,"it_about.html")

def contact(request):
    return render(request,"it_contact.html")

def scit_print(request):
    return render(request,"Scit_print.html")

def courses_list(req):
    return render(req,'Scit_courses_list.html')
