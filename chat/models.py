from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Chat(models.Model):
    name = models.CharField(max_length=80, default='test')
    members = models.ManyToManyField(User, related_name='chats')

    def __str__(self):
        return self.name


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messeges')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='A')
    message = models.TextField(max_length=256)

    def __str__(self):
        return self.message
