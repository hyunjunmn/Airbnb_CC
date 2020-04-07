from django.views.generic import ListView,DetailView
from django_countries import countries
from django.shortcuts import render
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
     
class RoomDetail(DetailView):
    model = models.Room
 

def search(request):
    city = request.GET.get("city","Anywhere")
    city = str.capitalize(city)
    room_types=models.RoomType.objects.all()
    return render(request,"rooms/search.html",{"city":city,"countries":countries,"room_types":room_types})
    
    
"""def room_detail(request,pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request,"rooms/detail.html",{'room':room})

    except models.Room.DoesNotExist:
        raise Http404()
   """ 
    
