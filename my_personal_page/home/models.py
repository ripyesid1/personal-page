from django.db import models

# Create your models here.

class User(models.Model):
    userName = models.CharField(max_length = 255)
    firstName = models.CharField(max_length = 255)
    lastName = models.CharField(max_length = 255)
    password = models.CharField(max_length = 100)

class Comment(models.Model):
    userName = models.CharField(max_length=255)
    comment = models.CharField(max_length=1000)

class Blog_Post(models.Model):
    title = models.CharField(max_length=400)
    author = models.CharField(max_length=510)
    date = models.DateField()
    postBody = models.CharField(max_length=10000)
    summary = models.CharField(max_length=200)

class project(models.Model):
    projectName = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    languages = models.CharField(max_length=120)
    summary = models.CharField(max_length=500)
    description = models.CharField(max_length=10000)
    githubLink = models.URLField(max_length=128)

