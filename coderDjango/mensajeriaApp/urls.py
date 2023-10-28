from django.urls import path
from . import views

urlpatterns = [
    path('', views.MessagesView.as_view(), name='chat_view'),
]
