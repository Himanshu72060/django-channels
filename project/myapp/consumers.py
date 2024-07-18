# # consumers.py
# from channels.consumer import SyncConsumer, AsyncConsumer


# class MySyncConsumer(SyncConsumer):
#     def websocket_connect(self, event):
#         print('WebSocket_Connect....', event)
#         self.send({
#             'type':'websocket.accept'
#         })

#     def websocket_receive(self, event):
#         print('Message Received....', event)

#     def websocket_disconnect(self, event):
#         print('WebSocket_DisConnected....', event)


# class MyAsyncConsumer(AsyncConsumer):
#     async def websocket_connect(self, event):
#         print('WebSocket_Connect....', event)

#     async def websocket_receive(self, event):
#         print('Message Received....')

#     async def websocket_disconnect(self, event):
#         print('WebSocket_DisConnected....')


# myapp/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer


class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))
