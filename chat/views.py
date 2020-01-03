from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

# Create your views here.
from chat.models import *


def index(request):
    chats=Chat.objects.filter(members__in=[request.user.id])
    return render(request,'index.html',locals())

def room(request, room_id):
    room_name_json=mark_safe(json.dumps(room_id))
    try:
        messages=Message.objects.filter(chat=room_id)

    except:
        error="Wrire"
        messages.delete()
    return render(request, 'room.html',locals())