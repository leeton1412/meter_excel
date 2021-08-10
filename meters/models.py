from django.db import models

# Create your models here.


class Meters(models.Model):

    Customer_Name = models.CharField('Customer Name', max_length=100, blank=False)
    Customer_Address = models.CharField(max_length=80, null=True, blank=True)
    Rate_Name = models.CharField(max_length=80, null=True, blank=True)
    Meter_Number = models.CharField(max_length=100, blank=False)
    Day_Rate = models.FloatField(max_length=100, null=True)
    Night_Rate = models.FloatField(null=True)
    Weekend_Rate = models.FloatField(null=True)

    def __str__(self):
        return self.Customer_Name
