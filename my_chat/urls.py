from django.contrib import admin
from django.urls import path, include
from .views import *

# http://127.0.0.1:8000/accounts/logout/
# http://127.0.0.1:8000/accounts/login/
# http://127.0.0.1:8000/chat/room_name
urlpatterns = [
    # path('accounts/login/', Login_Home.as_view(), name='Home_Login'),
    path('', Chat_Home.as_view(), name='chat_home'),
    path('<str:room_name>/', Chat_Room.as_view(), name='chat_room'),
    path('ui/chat_ui/', Chat_Ui.as_view(), name='chat_ui'),
    # path('<str:room_name>/', Chat_Room, name='room'),
]
