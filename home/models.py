from django.db import models

# Create your models here.

class Friends(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField(blank=True,null=True)
    image = models.FileField(upload_to = 'profile_pic')

class Gallery(models.Model):
    text = models.TextField(null=True,blank=True)
    image = models.FileField(upload_to = 'gallery')