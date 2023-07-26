import asyncio

from channels.generic.websocket import AsyncWebsocketConsumer


class EmailGeneratorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'email_generator'
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def send_message(self, event):
        message = event['message']
        await self.send(text_data=message)

    async def generate_messages(self, event):
        increment = event['increment']
        await self.send(text_data=f'Generated {increment} messages so far')


async def background_task(channel_layer):
    for increment in range(number_of_mail):
        await asyncio.sleep(1)  # Simulate some processing time
        await channel_layer.group_send('email_generator', {
            'type': 'generate_messages',
            'increment': increment
        })


async def start_background_task(channel_layer):
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, background_task, channel_layer)
