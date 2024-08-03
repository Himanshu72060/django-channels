from channels.generic.websocket import JsonWebsocketConsumer, AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync


class MyJsonWebsocketConsumer(JsonWebsocketConsumer):
    def connect(self):
        print("Websocket Connected.....")
        print("Channel Layer", self.channel_layer)
        print("Channel Name", self.channel_name)
        self.group_name = self.scope['url_route']['kwargs']['groupkaname']
        print("Group Name:", self.group_name)
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()
        # self.close()

    def receive_json(self, content, **kwargs):
        print("Message received from Clint....", content)
        # print("Type of Message received from Clint....", type(content))

        # self.send_json({'message':'Message from server to client'})
        for i in range(20):
            self.send_json({'message': str(i)})
            # sleep(1)

    def disconnect(self, close_code):
        print("Websocket Disconnected.....", close_code)


class MyAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print("Websocket Connected.....")
        await self.accept()
        # await self.close()

    async def receive_json(self, content, **kwargs):
        print("Message received from Clint....", content)
        # print("Type of Message received from Clint....", type(content))

        # await self.send_json({'message': 'Message from server to client'})
        # await self.close()
        for i in range(20):
            await self.send_json({'message': str(i)})
            # await asyncio.sleep(1)

    async def disconnect(self, close_code):
        print("Websocket Disconnected.....", close_code)
