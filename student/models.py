from django.db import models
import os

# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254,unique=True)
    phone = models.CharField(max_length=13)
    gender = models.CharField(choices=[("MALE","MALE"),("FEMALE","FEMALE"),("OTHER","OTHER")],max_length=50)
    dob = models.DateField()
    status = models.CharField(choices=[("APPROVED","APPROVED"),("NOT APPROVED","NOT APPROVED")],default="NOT APPROVED",max_length=50)
    image = models.ImageField(null=True, blank=True, upload_to='images/profiles/students/')
    institute = models.ForeignKey("franchise.Franchise",null=False,on_delete=models.CASCADE, to_field="id")
    class Meta:
        ordering = ['-id']
    def __str__(self):
        return f"{self.name} - {self.email}"
    def delete(self, *args, **kwargs):
        # Delete the associated image file before deleting the model instance
        if self.image:
            if os.path.isfile(self.image.path):
                try:
                   os.remove(self.image.path)
                except Exception as e:
                   print(e)
        super(Student, self).delete(*args, **kwargs)

class Enrollment(models.Model):
    student_id = models.ForeignKey("student.Student", on_delete=models.CASCADE, to_field="id")
    course_id = models.ForeignKey("student.Course", on_delete=models.CASCADE, to_field="id") 

    def __str__(self):
        return f"{self.student_id} - {self.course_id}"
    

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False,unique=True,max_length=50)
    price  = models.DecimalField(null=False,max_digits=10,decimal_places=2)
    details = models.TextField()
    tumbnail = models.ImageField(null=True, blank=True, upload_to='images/courses/')
    category = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name} - {self.category}"
    def delete(self, *args, **kwargs):
        # Delete the associated image file before deleting the model instance
        if self.tumbnail:
            if os.path.isfile(self.tumbnail.path):
                try:
                   os.remove(self.tumbnail.path)
                except Exception as e:
                   print(e)
        super(Course, self).delete(*args, **kwargs)

class Certificate(models.Model):
    id = models.AutoField(primary_key=True)
    certificate_no = models.CharField(null=False,blank=False,max_length=50,unique=True)
    Student_id = models.ForeignKey("student.Student", on_delete=models.CASCADE, to_field="id")
    Course_id = models.ForeignKey("student.Course",null=True,blank=True,on_delete=models.CASCADE, to_field="id")
    src = models.ImageField(null=True, blank=True, upload_to='images/certificates/')
    def __str__(self):
        return f"{self.Student_id} - {self.Course_id}"
    
    def delete(self, *args, **kwargs):
        # Delete the associated image file before deleting the model instance
        if self.src:
            if os.path.isfile(self.src.path):
                try:
                   os.remove(self.src.path)
                except Exception as e:
                   print(e)
        super(Certificate, self).delete(*args, **kwargs)

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=13)
    message = models.TextField(max_length=500)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} - {self.email}"




