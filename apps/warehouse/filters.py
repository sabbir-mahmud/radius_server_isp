# imports
from dataclasses import field

from django_filters import FilterSet

from .models import Warehouse, WarehouseCategory


# warehouse filter
class WarehouseFilter(FilterSet):
 class Meta:
  model = Warehouse
  fields = ['serial','category','status']

# category filter
class CategoryFilter(FilterSet):
 class Meta:
  model = WarehouseCategory
  fields = ['name']


