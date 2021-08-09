from django.contrib import admin
from .models import Meters
# Register your models here.


@admin.register(Meters)
class ViewAdmin(admin.ModelAdmin):
    pass
