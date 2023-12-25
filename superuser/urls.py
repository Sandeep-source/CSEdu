from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("",home),
    path("login",login),
    path("logout",logout),
    path("manage_student",manage_student,name="manage_student"),
    path("sign_up",sign_up),
    path("add_student",add_student),
    path("remove_student",remove_student),
    path("enroll_student",enroll_student),
    path("view_courses",view_courses),
    path("institute",institute),
    path("delete_student",action,name="action"),
    path("add_course",add_course),
    path("add_institute",add_institute),
    path("delete_institute",delete_institute),
    path("delete_course",delete_course),
    path("update_student",update_student),
    path("update_course",update_course),
    path("update_institute",update_institute),
    path("delete_enroll",delete_enroll),
    path("issue_certificate",issue_certificate),
    path("approve_student",approve_student),
    path("add_admin",add_admin),
    path("delete_certificate",delete_certificate),
    path("contact",contact),
    path("resolved_contact",resolved_contact),
    path("delete_contact",delete_contact),
    path("manage_admins",manage_admins),
    path("delete_admin",delete_admin),
    
    # path("update_admin",update_admin),
]