from django.urls import re_path

from . import consumers_chat

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers_chat.ChatConsumer.as_asgi()),
]