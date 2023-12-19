from django.shortcuts import render, redirect
from django.contrib.auth import login as Login,logout as Logout,authenticate
from django.contrib.auth.models import User
from student.models import Student, Course
from franchise.models import Franchise
from .forms import CourseForm, FranchiseForm

# Create your views here.


def home(req):
    if req.user.is_authenticated:
        return render(req,"Admin_dashboard.html")
    else:
        return render(req,"AdminPortal_login.html")

def login(req):
    username = req.POST["username"]
    password = req.POST["password"]
    user = authenticate(req,username=username,password=password)
    if user == None:
        return render(req,"AdminPortal_login.html")
    else:
        Login(req,user)
        return redirect("/superuser/")

def logout(req):
    Logout(req)
    return render(req,"AdminPortal_login.html")

def sign_up(req):
    return render(req,"AdminPortal_registration.html")

def manage_student(request):
    students = Student.objects.all()
    return render(request,"NViewStudent.html",context = {"students":students})


def action(request):
    print(request.POST)
    emails = request.POST.getlist("emails")
    for email in emails:
            print(email)
            student = Student.objects.get(email=email)
            if student:
                student.delete()
    return redirect("/superuser/manage_student")

def add_student(request):
    if request.method=="POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        dob = request.POST["dob"]
        password = request.POST["password"]
        image = request.POST["image"]
        gender = request.POST["gender"]
        student = Student.objects.create(
            name=name,
            email=email,
            phone=phone,
            dob=dob,
            password=password,
            image=image,
            gender=gender)
        student.save()
        return render(request,"NAddStudent.html",context={"success":True})
    return render(request,"NAddStudent.html")

def remove_student(request):
    return render(request,"NRemoveStudent.html")

def enroll_student(request):
    return render(request,"NAddStudent.html")

def institute(request):
    franchises = Franchise.objects.all()
    return render(request,"other_view.html",context={"franchises":franchises})

def view_courses(request):
    courses = Course.objects.all()
    return render(request,"View_courses.html", context={"courses":courses})

def add_course(request):
    form = CourseForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        form = CourseForm(None) 
    return render(request,"add_courses.html",context={"form":form})

def add_institute(request):
    form = FranchiseForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = FranchiseForm(None)
    return render(request,"other_add.html", context={"form":form})

def delete_institute(request):
    if request.user.is_authenticated:
        id = request.GET["id"]
        f = Franchise(id=id)
        f.delete()
    return redirect("/superuser/institute")

def delete_course(request):
    if request.user.is_authenticated:
        id = request.GET['id']
        try:
            course = Course.objects.get(id=id)
            course.delete()
        except e:
            print(e)
    return redirect("/superuser/view_courses")
        
