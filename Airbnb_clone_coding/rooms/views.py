from django.views.generic import ListView,DetailView
from django_countries import countries
from django.shortcuts import render
from . import models, forms
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
    
    form = forms.SearchForm()
    return render(request,"rooms/search.html",{"form":form})