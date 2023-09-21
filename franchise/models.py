from django.db import models

# Create your models here.


class Franchise(models.Model):
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

