from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as Login,logout as Logout,authenticate
from student.models import Student, Course, Enrollment, Certificate, Contact
from franchise.models import Franchise
from student.forms import StudentForm, EnrollmentForm,CertificateForm
from .forms import CourseForm, FranchiseForm, UserForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm

# Create your views here.

@login_required(login_url="/superuser/login")
def home(req):
    if req.user.is_superuser:
        return render(req,"Admin_dashboard.html")
    else:
        return redirect("/superuser/manage_student")

def login(req):
    if req.user.is_authenticated:
        return redirect("/superuser/")
    if req.method=="POST":
        username = req.POST["username"]
        password = req.POST["password"]
        user = authenticate(req,username=username,password=password)
        if user:
            Login(req,user)
            return redirect("/superuser/")
        else:
            return render(req,"AdminPortal_login.html",context={"message":"Incorrect username or password."})
    return render(req,"AdminPortal_login.html")
      
@login_required(login_url="/superuser/login")
def logout(req):
    Logout(req)
    return redirect("/superuser/login")

def sign_up(req):
    return render(req,"AdminPortal_registration.html")

@login_required(login_url="/superuser/login")
def manage_student(request):
    students = Student.objects.all()
    institute = 0
    status = ""
    if not request.user.is_superuser:
        students = Student.objects.filter(institute=request.user.last_name)
    else:
        if "institute" in request.GET:
            institute = int(request.GET["institute"])
            status = request.GET["status"]
            print("status",status,"institute",institute)
            if institute>0 and len(status)>0:
                students = Student.objects.filter(status=status,institute=institute)
            elif institute>0:
                students = Student.objects.filter(institute=institute)
            elif len(status)>0:
                students = Student.objects.filter(status=status)               
    institutes = Franchise.objects.all()
    return render(request,"NViewStudent.html",context = {"students":students,"institutes":institutes,"selected_institute":institute,"status":status})

@user_passes_test(lambda user: user.is_superuser,login_url="/unauthorized_access")
def action(request):
    print(request.POST)
    id = request.POST["id"]
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("/superuser/manage_student")

@login_required(login_url="/superuser/login")
def add_student(request):
    form = StudentForm(user=request.user, data=request.POST or None, files=request.FILES or None)
    print(form.is_valid)
    if request.method=="POST" and form.is_valid():
        form.save()
        print("under")
        form = StudentForm(user=request.user,data=None)
        return render(request,"NAddStudent.html",context={"success":True,"form":form})
    return render(request,"NAddStudent.html",context={"form":form})

@user_passes_test(lambda user: user.is_superuser,login_url="/unauthorized_access")
def remove_student(request):
    return render(request,"NRemoveStudent.html")

@user_passes_test(lambda user: user.is_superuser,login_url="/unauthorized_access")
def enroll_student(request):
    form = EnrollmentForm(request.POST or None, request.FILES or None)
    print(form.is_valid)
    enrollments = Enrollment.objects.all()
    if request.method=="POST" and form.is_valid():
        form.save()
        print("under")
        form = EnrollmentForm(None)
        return render(request,"Scit_student_enroll.html",context={"success":True,"form":form,"enrollments":enrollments})
    return render(request,"Scit_student_enroll.html",context={"form":form,"enrollments":enrollments})

@user_passes_test(lambda user: user.is_superuser,login_url="/unauthorized_access")
def institute(request):
    franchises = Franchise.objects.all()
    return render(request,"other_view.html",context={"franchises":franchises})

@user_passes_test(lambda user: user.is_superuser)
def view_courses(request):
    courses = Course.objects.all()
    return render(request,"View_courses.html", context={"courses":courses})

@user_passes_test(lambda user: user.is_superuser)
def add_course(request):
    form = CourseForm(request.POST or None,request.FILES or None)
    success = False
    if form.is_valid():
        form.save()
        form = CourseForm(None) 
        success = True
    return render(request,"Add_courses.html",context={"form":form,"success":success})

@user_passes_test(lambda user: user.is_superuser)
def add_institute(request):
    form = FranchiseForm(request.POST or None, request.FILES or None)
    success = False
    if form.is_valid():
        form.save()
        form = FranchiseForm(None)
        success = True
    return render(request,"other_add.html", context={"form":form,"success":success})

@user_passes_test(lambda user: user.is_superuser,login_url="/unauthorized_access")
def delete_institute(request):
        id = request.POST["id"]
        f = Franchise(id=id)
        f.delete()
        return redirect("/superuser/institute")

@user_passes_test(lambda user: user.is_superuser,login_url="/unauthorized_access")
def delete_course(request):
    id = request.POST['id']
    try:
        course = Course.objects.get(id=id)
        course.delete()
    except e:
        print(e)
    return redirect("/superuser/view_courses")

# def view_student(request):
#     id = request.GET["id"]
#     student = Student.objects.get(id=id)
#     form = StudentForm(student)
#     return render(request,"NUpdateStudent",context={"form":form,"id":id})

@user_passes_test(lambda user: user.is_superuser,login_url="/unauthorized_access")        
def update_student(request):
    id = request.GET["id"]
    print("id",id)
    student = get_object_or_404(Student,pk=id)
    form = StudentForm(user=request.user, data=request.POST or None, files=request.FILES or None, instance=student)
    if form.is_valid():
        form.save()
        return render(request,"NUpdateStudent.html",context={"form":form,"id":id,"message":"Student updated successfully."})
    return render(request,"NUpdateStudent.html",context={"form":form,"id":id})

@user_passes_test(lambda user: user.is_superuser,login_url="/unauthorized_access")
def update_course(request):
    id = request.GET["id"]
    print("id",id)
    course = get_object_or_404(Course,pk=id)
    form = CourseForm(request.POST or None, request.FILES or None, instance=course)
    if form.is_valid():
        form.save()
        return render(request,"update_courses.html",context={"form":form,"id":id,"updated":True})
    return render(request,"update_courses.html",context={"form":form,"id":id})

@user_passes_test(lambda user: user.is_superuser,login_url="/unauthorized_access")
def approve_student(request):
    id = request.GET["id"]
    student = get_object_or_404(Student,pk=id)
    student.status="APPROVED"
    student.save()
    return redirect("/superuser/manage_student")

@user_passes_test(lambda user: user.is_superuser,login_url="/unauthorized_access")
def update_institute(request):
    id = request.GET["id"]
    print("id",id)
    course = get_object_or_404(Franchise,pk=id)
    form = FranchiseForm(request.POST or None, request.FILES or None, instance=course)
    if form.is_valid():
        form.save()
    return render(request,"other_update.html",context={"form":form,"id":id})

@user_passes_test(lambda user: user.is_superuser,login_url="/unauthorized_access")
def delete_enroll(request):
    id = request.POST["id"]
    enrollment = Enrollment.objects.get(id=id)
    enrollment.delete()
    return redirect("/superuser/enroll_student")

@user_passes_test(lambda user: user.is_superuser,login_url="/unauthorized_access")
def issue_certificate(request):
    certificate = CertificateForm(request.POST or None, request.FILES or None)
    certificates = Certificate.objects.all()
    if request.method=="POST" and  certificate.is_valid():
        certificate.save()
    return render(request,"certificate.html",context={"form":certificate,"certificates":certificates})

@user_passes_test(lambda user: user.is_superuser,login_url="/unauthorized_access")
def add_admin(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
           form.save()
           return render(request,"TNAdmin.html",context={"form":form,"success":True})
    return render(request,"TNAdmin.html",context={"form":form})

@user_passes_test(lambda user: user.is_superuser,login_url="/unauthorized_access")
def delete_certificate(request):
    id = request.POST["id"]
    print("ID",id)
    certificate = Certificate.objects.get(id=id)
    certificate.delete()
    return redirect("/superuser/issue_certificate")

@user_passes_test(lambda user: user.is_superuser,login_url="/unauthorized_access")
def contact(request):
    contacts = Contact.objects.all()
    return render(request,"admin_contacts.html",context={"contacts":contacts})

@user_passes_test(lambda user: user.is_superuser,login_url="/unauthorized_access")
def resolved_contact(request):
    id = request.GET["id"]
    contact = Contact.objects.get(id=id)
    contact.resolved = True
    contact.save()
    return redirect("/superuser/contact")

@user_passes_test(lambda user: user.is_superuser,login_url="/unauthorized_access")
def delete_contact(request):
    id = request.POST["id"]
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect("/superuser/contact")

@user_passes_test(lambda user: user.is_superuser,login_url="/unauthorized_access")
def manage_admins(request):
    admins = User.objects.exclude(email="scitcomputer2019@gmail.com")
    for admin in admins:
        try:
            admin.last_name = Franchise.objects.get(id=admin.last_name)
        except Exception as e:
            print(e)
    return render(request,"TVAdmin.html",context={"admins":admins})

@user_passes_test(lambda user: user.is_superuser,login_url="/unauthorized_access")
def delete_admin(request):
    username = request.POST["username"]
    user = User.objects.get(username=username)
    user.delete()
    return redirect("/superuser/manage_admins")

def password_reset(request):
    form = PasswordResetForm(request.POST or None)
    if form.is_valid():
        form.save()