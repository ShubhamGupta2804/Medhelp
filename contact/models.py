from django.db import models
from datetime import datetime

# Create your models here.

class contact(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=50) 
    city = models.CharField(max_length=50) 
    message = models.CharField(max_length=500) 

def __str__(self):
    return self.fname
