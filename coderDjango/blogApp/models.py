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


class Resena(Articulo):
    score = models.DecimalField(max_digits=3, decimal_places=2, help_text="Puntuación de la reseña")
    review_date = models.DateField(help_text="Fecha de la reseña")


# Modelo hijo 2: Guia
class Guia(Articulo):
    topic = models.CharField(max_length=200, help_text="Tema de la guía")
    duration = models.PositiveIntegerField(help_text="Duración estimada de la guía (en minutos)")


class Noticia(Articulo):
    source = models.CharField(max_length=200, help_text="Fuente de la noticia")
    publication_date = models.DateField(help_text="Fecha de publicación de la noticia")


class Entrevista(Articulo):
    interviewed_person = models.CharField(max_length=200, help_text="Nombre del entrevistado")
    interviewed_person_position = models.CharField(max_length=200, help_text="Cargo del entrevistado")
    interview_date = models.DateField(help_text="Fecha de la entrevista")
    interviewer = models.CharField(max_length=200, help_text="Nombre del entrevistador")


# Modelo hijo 5: Tutorial
class Tutorial(Articulo):
    category = models.CharField(max_length=200, help_text="Categoría del tutorial")
    level = models.CharField(max_length=50, help_text="Nivel del tutorial (principiante, intermedio, avanzado)")
