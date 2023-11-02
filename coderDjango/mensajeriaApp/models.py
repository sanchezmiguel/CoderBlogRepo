from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    usuario_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats1',
                                  help_text="Usuario 1 en el chat.")
    usuario_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats2',
                                  help_text="Usuario 2 en el chat.")

    def __str__(self):
        return f"Chat entre {self.usuario_1} y {self.usuario_2}"


class Message(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora de creación del mensaje.")
    texto = models.TextField(help_text="Texto del mensaje.")
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, help_text="Chat al que pertenece este mensaje.")

    def __str__(self):
        return f"{self.fecha_creacion.strftime('%Y-%m-%d %H:%M')} - {self.texto}"
