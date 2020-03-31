from math import ceil
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models
# Create your views here.

def all_rooms(request):
    page = int(request.GET.get("page",1))
    room_list = models.Room.objects.all()  #query sets
    paginator = Paginator(room_list, 10,orphans=5) #orpahns남은 자료들을 그 전페이지로 이어붙임
    rooms = paginator.page(int(page))
  #  print(vars(rooms.paginator))
    return render(request,"rooms/home.html",{"page":rooms})