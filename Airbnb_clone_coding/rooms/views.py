from django.views.generic import ListView
from . import models
# Create your views here.

class HomeView(ListView):
      """Home View Definition"""
      
      model = models.Room
      paginate_by =10
      paginate_orphans = 5
      ordering = "created"
     # page_kwarg = "page"

'''def all_rooms(request):
    page = int(request.GET.get("page",1))
    room_list = models.Room.objects.all()  #query sets
    paginator = Paginator(room_list, 10,orphans=5) #orpahns남은 자료들을 그 전페이지로 이어붙임
    try:
        rooms = paginator.page(int(page))
        return render(request,"rooms/home.html",{"page":rooms})
    except EmptyPage:
      return redirect("/")
      #rooms = paginator.page(1)
  #  print(vars(rooms.paginator))
    '''