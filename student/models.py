from django.db import models

# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254,unique=True)
    phone = models.CharField(max_length=13)
    gender = models.CharField(choices=[("MALE","MALE"),("FEMALE","FEMALE"),("OTHER","OTHER")],max_length=50)
    dob = models.DateField()
    image = models.ImageField(null=True, blank=True, upload_to='images/profiles/students/')
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name} - {self.email}"

class Enrollment(models.Model):
    student_id = models.ForeignKey("student.Student", on_delete=models.CASCADE, to_field="id")
    course_id = models.ForeignKey("student.Course", on_delete=models.CASCADE, to_field="id") 

    def __str__(self):
        return f"{self.student_id} - {self.course_id}"

class Course(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(null=False,unique=True,max_length=50)
    price  = models.DecimalField(null=False,max_digits=10,decimal_places=2)
    details = models.TextField()
    tumbnail = models.ImageField(null=True, blank=True, upload_to='images/courses/')
    category = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name} - {self.category}"

class Certificate(models.Model):
    id = models.AutoField(primary_key=True)
    Student_id = models.ForeignKey("student.Student", on_delete=models.CASCADE, to_field="id")
    Course_id = models.ForeignKey("student.Course",null=True,blank=True,on_delete=models.CASCADE, to_field="id")
    src = models.ImageField(null=True, blank=True, upload_to='images/certificates/')
    def __str__(self):
        return f"{self.Student_id} - {self.Course_id}"


