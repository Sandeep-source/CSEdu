from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student, Course, Certificate, Enrollment
from django.contrib.auth import authenticate,login as Login,logout as Logout

# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return redirect("/student/login")
    print(request.user.email)
    student = Student.objects.get(email=request.user.email)
    courses_pursued = Course.objects.filter(enrollment__student_id=student).prefetch_related('certificate_set')
    return render(request,'Scit_student_dashboard.html',context={"courses":courses_pursued})

def verify_certificate(request):
    return render(request,'verify_certificate.html')

def login(request):
    if request.user.is_authenticated:
        return redirect("/student/")
    if request.method == "POST":
       username = request.POST['username']
       password = request.POST["password"]
       user = authenticate(request,username=username,password=password)
       if user == None:
           return render(request,'Scit_Student_login.html',context={"failed":True})
       else:
           Login(request,user)
           return redirect("/student/")        
    return render(request,'Scit_Student_login.html')

def forget_password(req):
    return render(req,'Scit_Student_forget.html')

def logout(request):
    Logout(request)
    return redirect('/student/login')


def signup(request):
    return render(request,'Scit_Student_enroll.html')

def purchase(request):
    return HttpResponse("<h1> Purchase Page")
