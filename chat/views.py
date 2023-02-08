from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from chat.models import Room,Message
import datetime
from chat.server import finddiff

# Create your views here.
def home(request):
    return render(request,'home.html')


def room(request,room):
    room_details = Room.objects.get(name=room)
    username = request.GET.get('username')
    print(room_details,username)
    return render(request,'room.html',{
        'username' :username,
        'room':room,
        'room_details' : room_details
    })

def checkview(request):
    room = request.POST['room']
    username = request.POST['username']
    if(Room.objects.filter(name=room).exists()):
        return redirect('/'+room+'?username='+username)
    #if not exists
    new_room = Room.objects.create(name=room)
    new_room.save()
    return redirect('/'+room+'?username='+username)

def getmessages(request,room):
    room_details= Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    s = {}
    j = 0
    for i in (list(messages)):
        time = i.time
        curr_time = datetime.datetime.now()
        mess_time = datetime.datetime.strptime(time,'%Y-%m-%d %H:%M:%S')
        l = finddiff(curr_time,mess_time)
        seconds = int(l[0])
        mins =int( l[1])
        hours =int( l[2])
        days =int( l[3])
        months =int( l[4])
        years=int( l[5])
        if(years==0):
            if months!=0:
                if(months<=1) :  res_str =str( months)+" month ago"
                else : res_str =str( months)+" months ago"
            else:
                if days!=0:
                    if(days<=1) :  res_str = str(days)+" day ago"
                    else : res_str =str( days)+" days ago"
                else:
                    if hours!=0:
                        if(hours<=1) :  res_str =str( hours)+" hour ago"
                        else : res_str = str(hours)+" hours ago"
                    else:
                        if mins!=0:
                            if(mins<=1) :  res_str =str( mins)+" min ago"
                            else : res_str = str(mins)+" mins ago"
                        else:
                            if seconds!=30:
                                if(seconds<=1) :  res_str = str(seconds)+" second ago"
                                else : res_str = str(seconds)+" seconds ago"
        else:
            if(years<=1) :  res_str = str(years)+" year ago"
            else : res_str = str(years)+" years ago"
        s[j] = res_str
        j+=1
    return JsonResponse(
        {
            "messages" :list(messages.values()),
            "time_dict" : s
        }
    )

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    now = datetime.datetime.now()
    time = str(now.strftime("%Y-%m-%d %H:%M:%S"))
    new_message = Message.objects.create(value=message,user=username,room=room_id,time=time)
    new_message.save()
    return HttpResponse("Message sent")