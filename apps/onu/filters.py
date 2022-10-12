# imports
from django_filters import FilterSet

from .models import Onu


#* Onu Filter
class OnuFilter(FilterSet):
 class Meta:
  model = Onu
  fields = ['mac','status']
