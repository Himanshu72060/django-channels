from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/some_path/', consumers.MyConsumer.as_asgi()),
]

    # path('ws/ac/', consumers.MyAsyncConsumer.as_asgi()),
