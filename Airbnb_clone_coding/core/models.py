from django.db import models

# Create your models here.
class TimeStampedModel(models.Model)
 """Time Stamp model"""
 
    created = models.DateTimeField()
    updated = models.DateTimeField()
    