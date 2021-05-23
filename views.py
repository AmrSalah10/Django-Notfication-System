from django.db.models import query
import Notification
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from notifications.signals import notify


# Create your views here.

def index(request):
    members = User.objects.exclude(is_staff=True)
    return render(request,'index.html', {'members':members})

def logout_view(request):
    logout(request)
    return redirect('login')


# Send message to individual user
def sendMsg(request):
    sender = User.objects.get(username=request.user)
    receiver = User.objects.get(id=request.POST.get('member_id'))
    notify.send(sender, recipient=receiver, verb='Message', description=request.POST.get('message'))
    return redirect('index')
  
 
# Send message to all users once
def sendMsgAll(request):
    sender = User.objects.get(username=request.user)
    receiver = User.objects.all()
    notify.send(sender, recipient=receiver, verb='Message', description=request.POST.get('message'))
    return redirect('index') 

