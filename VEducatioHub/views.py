from django.shortcuts import render
from .forms import FranciseForm
from student.models import Course

def index(request):
    form = FranciseForm(request.POST or None)
    courses = Course.objects.all()[:6]
    return render(request,"index.html",context={"form":form,"courses":courses})

def home(request):
    courses = Course.objects.all()[:6]
    return render(request,"index.html",context={"courses":courses})

def home_dark(request):
    courses = Course.objects.all()[:6]
    return render(request,"it_home_dark.html",context={"courses":courses})

def about(request):
    return render(request,"it_about.html")

def contact(request):
    return render(request,"it_contact.html")

def scit_print(request):
    return render(request,"Scit_print.html")

def courses_list(req):
    courses = Course.objects.all()
    return render(req,'Scit_courses_list.html',context={"courses":courses})
