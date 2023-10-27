# from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Articulo(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='articulo_images/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articulos")

    def __str__(self):
        return self.title
