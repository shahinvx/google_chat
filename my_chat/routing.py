from django.urls import re_path
#import my_chat.consumers
from . import consumers

webcsocet_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatRoomConsumer.as_asgi()),
]
