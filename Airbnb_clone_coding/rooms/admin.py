from django.contrib import admin
from .import models



@admin.register(models.RoomType,models.Facility,models.Amenity,models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Definition"""

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    pass
    """Room Admin Definition"""
    
@admin.register(models.photo)
class PhotoAdmin(admin.ModelAdmin):
    pass