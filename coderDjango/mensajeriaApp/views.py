from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from .models import Chat, Message


class EnviarMensajeView(LoginRequiredMixin, View):
    model = Message
    success_url = '/pages'

    def post(self, request):
        # Obtén el ID del receptor y el mensaje del formulario
        receptor_id = request.POST.get('receptor')
        mensaje = request.POST.get('mensaje')

        try:
            # Verifica si el receptor existe
            receptor = User.objects.get(id=receptor_id)
        except User.DoesNotExist:
            receptor = None

        if receptor and mensaje:
            # Crea un nuevo chat si aún no existe uno entre el remitente y el receptor
            chat, created = Chat.objects.get_or_create(usuario_1=request.user, usuario_2=receptor)

            # Crea un nuevo mensaje en el chat
            message = Message(chat=chat, texto=mensaje)
            message.save()

        # Redirige de vuelta a la página de chats del usuario
        return redirect('user_chats', user_id=receptor_id)


class MessagesView(LoginRequiredMixin, View):
    model = Chat
    success_url = '/pages'

    def get(self, request):
        # Obtener todos los usuarios excepto request.user
        all_users = User.objects.exclude(username=request.user.username)

        # Obtener todos los chats en los que el usuario está involucrado
        user_chats = Chat.objects.filter(usuario_1=request.user) | Chat.objects.filter(usuario_2=request.user)

        # Obtener todos los mensajes de esos chats
        messages = Message.objects.filter(chat__in=user_chats)

        context = {
            'all_users': all_users,
            'user_chats': user_chats,
            'messages': messages
        }

        return render(request, 'mensajeriaApp/messages.html', context)


class UserChatsView(LoginRequiredMixin, View):
    model = Chat
    success_url = '/pages'

    def get(self, request, user_id):
        try:
            # Obtén el usuario seleccionado por su ID
            selected_user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            # Maneja el caso en el que el usuario no existe
            selected_user = None

        if selected_user:
            # Obtener el chat entre el usuario logueado y el usuario seleccionado
            user_chat = Chat.objects.filter(
                (Q(usuario_1=request.user, usuario_2=selected_user) | Q(usuario_1=selected_user, usuario_2=request.user))
            ).first()

            if user_chat:
                # Obtener todos los mensajes de ese chat
                messages = Message.objects.filter(chat=user_chat)
            else:
                messages = []

            context = {
                'selected_user': selected_user,
                'user_chat': user_chat,
                'messages': messages
            }
        else:
            # Puedes manejar el caso en el que el usuario no existe
            context = {
                'selected_user': None,
                'user_chat': None,
                'messages': []
            }

        return render(request, 'mensajeriaApp/user_chats.html', context)
