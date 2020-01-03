from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

from chat.models import *


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )


        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data)
        chat=Chat.objects.get(id=text_data_json['chat'])
        user=User.objects.get(id=int(text_data_json['user']))
        message = text_data_json['message']
        create_msg=Message(chat=chat,autor=user,message=message)
        create_msg.save()

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message':text_data_json['message'] ,
                'author':int(text_data_json['user'])
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        author_row= event['author']
        author=User.objects.get(id=int(author_row)).username

         # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'author':author,
            'author_id':author_row
        }))
