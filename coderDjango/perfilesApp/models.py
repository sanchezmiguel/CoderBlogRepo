from django.db import models


# Create your models here.
class CreatorProfile(models.Model):
    name = models.CharField(max_length=100,unique=True)
    position=models.CharField(max_length=100,default="")
    bio = models.TextField()
    email = models.EmailField()
    image = models.ImageField(upload_to='creator_images', blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    github = models.URLField(max_length=200, blank=True, null=True)
