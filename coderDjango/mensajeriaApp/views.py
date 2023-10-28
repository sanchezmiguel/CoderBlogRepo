from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from .models import Chat, Message

class MessagesView(LoginRequiredMixin, View):
    model = Chat
    success_url = '/pages'

    def get(self, request):
        # Obtener todos los usuarios
        all_users = User.objects.all()

        # Obtener todos los chats en los que el usuario está involucrado
        user_chats = Chat.objects.filter(usuario_1=request.user) | Chat.objects.filter(usuario_2=request.user)

        # Obtener todos los mensajes de esos chats
        messages = Message.objects.filter(chat__in=user_chats)

        context = {
            'all_users': all_users,
            'user_chats': user_chats,
            'messages': messages
        }

        return render(request, 'mensajeriaApp/chat.html', context)
