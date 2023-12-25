from django.db import models
import os

# Create your models here.


class Franchise(models.Model):
    id = models.AutoField(primary_key=True)
    centre_name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state  = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    office_image = models.ImageField(null=True, blank=True, upload_to='images/franchise/')
    email = models.EmailField(max_length=254)
    head_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    head_email_address = models.EmailField(max_length=254)
    def __str__(self):
        return f"{self.centre_name} - {self.city},{self.state}"
    class Meta:
        ordering = ['-id']

    def delete(self, *args, **kwargs):
        # Delete the associated image file before deleting the model instance
        if self.office_image:
            if os.path.isfile(self.office_image.path):
                try:
                   os.remove(self.office_image.path)
                except Exception as e:
                   print(e)
        super(Franchise, self).delete(*args, **kwargs)

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    highest_qualification = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    profile = models.ImageField(null=True, blank=True, upload_to='images/profiles/teachers/')
    def __str__(self):
        return f"{self.name} - {self.field_of_study}"
    def delete(self, *args, **kwargs):
        # Delete the associated image file before deleting the model instance
        if self.profile:
            if os.path.isfile(self.profile.path):
                try:
                   os.remove(self.profile.path)
                except Exception as e:
                   print(e)
        super(Teacher, self).delete(*args, **kwargs)
    
    



