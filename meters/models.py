from django.db import models

# Create your models here.


class Meters(models.Model):

    customer_name = models.CharField(max_length=100, blank=True, null=True)
    customer_address = models.CharField(max_length=80, null=True, blank=True)
    rate_name = models.CharField(max_length=80, null=True, blank=True)
    meter_number = models.CharField(max_length=100, blank=False, null=True)
    day_rate = models.FloatField(max_length=100, null=True)
    night_rate = models.FloatField(null=True)
    weekend_rate = models.FloatField(null=True)
    weekend_night_rate = models.FloatField(null=True)
    weekend_day_rate = models.FloatField(null=True)
    cost_for_day_rate = models.FloatField(null=True)
    cost_for_night_rate = models.FloatField(null=True)
    cost_for_weekend_rate = models.FloatField(null=True)
    cost_for_weekend_day_rate = models.FloatField(null=True)
    cost_for_weekend_night_rate = models.FloatField(null=True)
    total_energy_cost = models.FloatField(null=True)
    first_reading_day = models.IntegerField(null=True)
    second_reading_day = models.IntegerField(null=True)
    first_reading_night = models.IntegerField(null=True)
    second_reading_night = models.IntegerField(null=True)
    first_reading_weekend = models.IntegerField(null=True)
    second_reading_weekend = models.IntegerField(null=True)
    first_weekend_day = models.IntegerField(null=True)
    second_weekend_day = models.IntegerField(null=True)
    first_weekend_night = models.IntegerField(null=True)
    second_weekend_night = models.IntegerField(null=True)

    #def __str__(self):
        #return self.customer_name
