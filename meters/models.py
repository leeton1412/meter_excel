from django.db import models

# Create your models here.


class Meters(models.Model):

    customer_name = models.CharField(max_length=100, blank=False)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    meter_number = models.CharField(max_length=100, blank=False)
    rate_name = models.CharField(max_length=100, blank=False)
    day_rate = models.IntegerField()
    night_rate = models.IntegerField()
    weekend_Rate = models.IntegerField()

    def __str__(self):
        return self.customer_name
