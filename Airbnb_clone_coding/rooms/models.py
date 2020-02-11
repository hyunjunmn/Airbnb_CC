from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
#from users import models as user_models

# Create your models here.

class AbstractItem(core_models.TimeStampedModel):
    
    """abstract Item"""
    name = models.CharField(max_length=80)
    
    class Meta:
        abstract = True
    def __str__ (self):
        return self.name
   
class RoomType(AbstractItem):
    """Roomtype Model definition"""
    class Meta: # Meta클래스 : meta data를 제공해주는 클래스
        verbose_name = "Room Type"
        ordering = ['name']    #순서를 정해주는 명령어 name ,-created,-ordering_date ... 
    pass   
  
class Amenity (AbstractItem):
    """Amenity Model definition"""
    pass

    class Meta:
        verbose_name_plural = "Amenities"

class Facility(AbstractItem):
    """Facility Model Definition"""
    class Meta:
        verbose_name_plural = "Facilites"
    pass
 
 
class HouseRule(AbstractItem):
    """HouseRule Model Definition"""
    class Meta:
        verbose_name = "House Rule"
    
    pass

class photo(core_models.TimeStampedModel):
    
    """Photo model definition"""
    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room",related_name = "photos",on_delete=models.CASCADE) #그냥 ROOM으로 하면 파이썬은 위에서 밑으로 읽기때문에 room클래스가 없어서 읽어오지 못한다. 
    #하지만""을 하게되면 string으로 읽게되서 자동으로 인식한다
    def __str__(self):
        return self.caption

class Room(core_models.TimeStampedModel):
    """Room Model Definition"""
    
    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length =140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host  = models.ForeignKey("users.User", related_name = "rooms", on_delete=models.CASCADE)#다른 사용자와 연결해주는 명령어 Foreignkey(1대 다수) #cascade는 다같이 삭제됨(폭포수)
    room_type = models.ForeignKey("RoomType",related_name = "rooms",on_delete=models.SET_NULL, null=True) #user를 삭제했을 때 on_delete를 이용해서 같이 지울 지 말지 결정함
    amenities = models.ManyToManyField("Amenity",related_name = "rooms",blank =True)
    facilities = models.ManyToManyField("Facility",related_name = "rooms",blank =True)
    house_rules = models.ManyToManyField("HouseRule",related_name = "rooms",blank =True)
    """DJNAGO안에서 자동으로 STRING형식을 읽어줌 상하관계와 연관이 없어짐"""
    
    def __str__(self):
        return self.name
    
    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.rating_average()
        return all_ratings / len(all_reviews)
        