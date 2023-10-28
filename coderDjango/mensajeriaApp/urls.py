from django.urls import path
from . import views

urlpatterns = [
    path('', views.MessagesView.as_view(), name='messages'),
    path('<int:user_id>/', views.UserChatsView.as_view(), name='user_chats'),
    path('enviar_mensaje/', views.EnviarMensajeView.as_view(), name='enviar_mensaje'),
]
