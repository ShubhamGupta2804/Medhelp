from django.db import models
from datetime import datetime

# Create your models here.

class List_medicines(models.Model):
    medicineName = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    expiry = models.DateField(default=datetime.now, blank=False) 

def __str__(self):
    return self.medicineName
