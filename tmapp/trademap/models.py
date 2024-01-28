from django.db import models

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=40)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    profession = models.CharField(max_length=40)

class JobPostings(Account):
    jobs = [
        ('Plumber', 'Plumber'),
        ('Carpenter', 'Carpenter'),
        ('Electrician', 'Electrician'),
        ('Landscaper', 'Landscaper'),
        ('Painter or Decorator', 'Painter or Decorator'),
        ('Other', 'Other'),
        ]
    user = models.CharField(max_length=40)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=40)
    cost_offer = models.IntegerField()
    profession_type = models.CharField(max_length=40, choices= jobs)
    contact = models.CharField(max_length = 15, default = '')
    location = models.CharField(max_length = 100, default = '')

    
