import asyncio
import json

from channels.generic.websocket import AsyncWebsocketConsumer


class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        while True:
            message = await self.receive_json()
            await self.send_json({'echo': message})