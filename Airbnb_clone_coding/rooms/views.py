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
    country = request.GET.get("country","KR") 
    room_type =int(request.GET.get("room_type",0))
    
    price = int(request.GET.get("price",0))
    guests = int(request.GET.get("guests",0))
    bedrooms = int(request.GET.get("bedrooms",0))
    beds = int(request.GET.get("beds",0))
    baths = int(request.GET.get("baths",0))
    instant=request.GET.get("instant",False)
    superhost=request.GET.get("superhost",False)
    s_amenities = request.GET.getlist("amenities")
    s_facilities = request.GET.getlist("facilities")
        
    form = {"city":city,"s_room_type":room_type,"s_country":country,"price":price,"guests":guests,"bedrooms":bedrooms,
             "beds":beds,"baths":baths,"s_amenities":s_amenities,"s_facilities":s_facilities,"instant":instant,"superhost":superhost}
  
    room_types=models.RoomType.objects.all()  
    amenities = models.Amenity.objects.all()
    facilities= models.Facility.objects.all()
    choices = {"countries":countries,"room_types":room_types,"amenities":amenities,"facilities":facilities}
    return render(request,"rooms/search.html",{**form,**choices})

"""def room_detail(request,pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request,"rooms/detail.html",{'room':room})

    except models.Room.DoesNotExist:
        raise Http404()
   """ 
    
