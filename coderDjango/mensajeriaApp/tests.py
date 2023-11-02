from django.test import TestCase
from django.contrib.auth.models import User
from .models import Chat, Message


class ChatModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configuración de objetos de prueba una vez para el conjunto de pruebas
        user1 = User.objects.create(username='usuario1')
        user2 = User.objects.create(username='usuario2')
        Chat.objects.create(usuario_1=user1, usuario_2=user2)

    def test_str_representation(self):
        chat = Chat.objects.get(id=1)
        expected_str = f"Chat entre {chat.usuario_1} y {chat.usuario_2}"
        self.assertEqual(str(chat), expected_str)


class MessageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configuración de objetos de prueba una vez para el conjunto de pruebas
        user1 = User.objects.create(username='usuario1')
        user2 = User.objects.create(username='usuario2')
        chat = Chat.objects.create(usuario_1=user1, usuario_2=user2)
        Message.objects.create(texto='Hola', chat=chat)

    def test_str_representation(self):
        message = Message.objects.get(id=1)
        expected_str = f"{message.fecha_creacion.strftime('%Y-%m-%d %H:%M')} - {message.texto}"
        self.assertEqual(str(message), expected_str)

    def test_message_relationship(self):
        message = Message.objects.get(id=1)
        chat = message.chat
        self.assertTrue(isinstance(chat, Chat))
