from django.views.generic import ListView
from django.urls import reverse
from django.shortcuts import render,redirect
from . import models
# Create your views here.

class HomeView(ListView):
      """Home View Definition"""
      
      model = models.Room
      paginate_by =10
      paginate_orphans = 5
      ordering = "created"
      context_object_name = "rooms"
     # page_kwarg = "page"
     
def room_detail(request,pk):
    try:
        room = models.Room.objects.get(pk=pk)
    except models.Room.DoesNotExist:
        return redirect(reverse("core:home"))
    
    return render(request,"rooms/detail.html",{'room':room})

