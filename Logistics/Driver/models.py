import email
from django.db import models
from django.forms import CharField, FileField

# Create your models here.
class Driver_Detail(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=300)
    vehicle_registration_number = models.CharField(max_length=100)
    driving_licence_number = models.CharField(max_length=100)
    # registration_card_photo = models.FileField(blank=True,null=True)
    # driving_licence_photo = models.FileField(blank=True,null=True)
    # vehicle_registration_number = models.ImageField(upload_to='images/')
    # driving_licence_number = models.ImageField(upload_to='images/')


    

