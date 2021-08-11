from django.contrib import admin
from .models import Meters
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
# Register your models here.


@admin.register(Meters)
class ViewAdmin(ImportExportModelAdmin):
    pass


class MeterResource(resources.ModelResource):

    class Meta:
        model = Meters
        fields = ('customer_name', 'customer_address', 'meter_number', 
            'day_rate', 'night_rate', 'weekend_rate', 
            'cost_for_day_rate', 'cost_for_night_rate', 'cost_for_weekend_rate', 
            'total_energy_cost')
        exclude = ('rate_name')
