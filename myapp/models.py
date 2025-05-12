from django.db import models
# from django.utils import timezone
from datetime import date

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    services = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()
    date = models.DateField(default=date.today)
   


    def __str__(self):
        return self.name


