from django.shortcuts import render
from django.views import View


class ChatView(View):

    def get(self,request):
        return render(request, "chat.html")

class RoomView(View):

    def get(self,request,room_name):
        return render(request, "room.html", context={"room_name": room_name})