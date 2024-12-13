from django.db import models

# Create your models here.

class User(models.Model):
    userName = models.CharField(max_length = 255)
    firstName = models.CharField(max_length = 255)
    lastName = models.CharField(max_length = 255)
    password = models.CharField(max_length = 100)
