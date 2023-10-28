from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    usuario_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats1')
    usuario_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats2')

    def __str__(self):
        return f"Chat entre {self.usuario_1} y {self.usuario_2}"


class Message(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    texto = models.TextField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fecha_creacion.strftime('%Y-%m-%d %H:%M')} - {self.texto}"
