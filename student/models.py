from django.db import models

# Create your models here.

class Student(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=13)
    gender = models.CharField(choices=[("MALE","MALE"),("FEMALE","FEMALE"),("OTHER","OTHER")],max_length=50)
    dob = models.DateField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Enrollment(models.Model):
    student_id = models.ForeignKey("student.Student", on_delete=models.CASCADE, to_field="id")
    course_id = models.ForeignKey("student.Course", on_delete=models.CASCADE, to_field="id") 

class Course(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(null=False,unique=True,max_length=50)
    price  = models.DecimalField(null=False,max_digits=10,decimal_places=2)
    details = models.TextField()

class Frencise(models.Model):
    id = models.BigIntegerField(primary_key=True)
    centre_name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state  = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    email = models.EmailField(max_length=254)
    head_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    head_email_address = models.EmailField(max_length=254)

class Certificate(models.Model):
    id = models.AutoField(primary_key=True)
    Student_id = models.ForeignKey("student.Student", on_delete=models.CASCADE, to_field="id")

