from django.shortcuts import render
from .forms import FranciseForm
from student.models import Course
from student.forms import ContactForm

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
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request,"it_contact.html",context={"message":"Thanks for contacting us. Our team will soon contact you."})
    return render(request,"it_contact.html")

def scit_print(request):
    return render(request,"Scit_print.html")

def courses_list(req):
    courses = Course.objects.all()
    return render(req,'Scit_courses_list.html',context={"courses":courses})

def unauthorized_access(request):
    return render(request,"unauthorized_access.html")
