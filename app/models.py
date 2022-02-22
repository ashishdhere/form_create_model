from datetime import datetime
from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    contact = models.CharField(max_length=10)
    address = models.CharField(max_length=40)
    date = models.DateField()
    
    def __str__(self):
        return self.username