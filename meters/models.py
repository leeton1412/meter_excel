from django.db import models

# Create your models here.


class Meters(models.Model):

    customer_name = models.CharField('Customer Name', max_length=100, blank=True)
    customer_address = models.CharField(max_length=80, null=True, blank=True)
    rate_name = models.CharField(max_length=80, null=True, blank=True)
    meter_number = models.CharField(max_length=100, blank=False)
    day_rate = models.FloatField(max_length=100, null=True)
    night_rate = models.FloatField(null=True)
    weekend_rate = models.FloatField(null=True)

    def __str__(self):
        return self.Customer_Name
