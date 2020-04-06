from django.views.generic import ListView,DetailView
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
    city = request.GET.get("city")
    city = str.capitalize(city)
    return render(request,"rooms/search.html",{"city":city})
    
    
"""def room_detail(request,pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request,"rooms/detail.html",{'room':room})

    except models.Room.DoesNotExist:
        raise Http404()
   """ 
    
