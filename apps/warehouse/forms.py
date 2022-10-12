# imports 
from dataclasses import field

from django.forms import ModelForm

from .models import Warehouse, WarehouseCategory


# warehouse category form
class WarehouseCategoryForm(ModelForm):
 class Meta:
  model = WarehouseCategory
  fields = '__all__'


# warehouse product form
class WarehouseProductForm(ModelForm):
 class Meta:
  model = Warehouse
  fields = '__all__'
