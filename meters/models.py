from django.db import models

# Create your models here.


class Meters(models.Model):

    customerName = models.CharField(max_length=100, blank=False)
    customerAddress = 
    meterNumber = models.CharField(max_length=100, blank=False)
    rateName = models.CharField(max_length=100, blank=False)
    dayRate = 
    nightRate = models.IntegerField()
    weekendRate =  models.IntegerField()


