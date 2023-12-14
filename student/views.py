from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.

def home(request):
    return render(request,'Scit_student_dashboard.html')

def verify_certificate(request):
    return render(request,'verify_certificate.html')

def login(request):
    return render(request,'Scit_Student_login.html')

def forget_password(req):
    return render(req,'Scit_Student_forget.html')

def logout(request):
    return HttpResponse("<h1> student logout")


def signup(request):
    return render(request,'Scit_Student_enroll.html')

def purchase(request):
    return HttpResponse("<h1> Purchase Page")
