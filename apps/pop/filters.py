# imports
from django_filters import FilterSet

from .models import Pop


#* PopFilter
class PopFilter(FilterSet):
 class Meta:
  model = Pop
  fields = ['name']
