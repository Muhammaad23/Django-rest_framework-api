from django.urls import path
from . import views

urlpatterns = [
    path('chats/', views.chat_list, name='chat-list'),
    path('chats/send/', views.send_message, name='send-message'),
]
