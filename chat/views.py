from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
import json
from datetime import datetime
# Create your views here.
from chat.models import *

@login_required
def index(request):
    chats=Chat.objects.filter(members__in=[request.user.id])
    return render(request,'index.html',locals())


def room(request, room_id):
    x1=datetime.now()
    room_name_json=mark_safe(json.dumps(room_id))
    try:
        messages=Message.objects.filter(chat=room_id)

    except:
        error="Wrire"
        messages.delete()
    x2=datetime.now()
    print(x2-x1)
    return render(request, 'room.html',locals())

def login(request):
    error=''
    if request.method=='POST':
        name= request.POST.get('login-name','')
        password= request.POST.get('login-password','')
        user = auth.authenticate(username=name, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            print('asd')
            return render(request,'login.html',{'error':'Проверте логин и пароль'})
    return render(request,'login.html',locals())

def registration(request):
    form = UserCreationForm()
    if request.POST:
        new_form = UserCreationForm(request.POST)
        if new_form.is_valid():
            new_form.save()
            aut = auth.authenticate(username=new_form.cleaned_data['username'],
                                    password=new_form.cleaned_data['password2'])
            auth.login(request, aut)