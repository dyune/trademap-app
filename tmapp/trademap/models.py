from django.db import models

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=40)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    profession = models.CharField(max_length=40)
