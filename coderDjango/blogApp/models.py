from django.contrib.auth.models import User
from django.db import models


class Articulo(models.Model):
    title = models.CharField(max_length=200, help_text="Título del artículo.")
    subtitle = models.CharField(max_length=200, help_text="Subtítulo del artículo.")
    text = models.TextField(blank=True, help_text="Texto del artículo. Puede estar en blanco si es necesario.")
    image = models.ImageField(upload_to='articulo_images/', blank=True, null=True,
                              help_text="Imagen asociada al artículo.")
    created = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora de creación del artículo.")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articulos",
                               help_text="Autor del artículo. Enlazado a un usuario.")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"
