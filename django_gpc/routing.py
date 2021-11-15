from typing import ChainMap
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import my_chat.routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            my_chat.routing.webcsocet_urlpatterns
        )
    ),
})
