from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from .models import ChatMessage
from django.db.models import Prefetch

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    message = ChatMessage.objects.filter(chatroom="chat_"+room_name)
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'messages' : message
    })