from django.contrib import admin

from .models import Warehouse, WarehouseCategory

# Register your models here.
admin.site.register(WarehouseCategory)
admin.site.register(Warehouse)
