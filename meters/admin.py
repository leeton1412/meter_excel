from django.contrib import admin
from .models import Meters
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(Meters)
class ViewAdmin(ImportExportModelAdmin):
    pass
