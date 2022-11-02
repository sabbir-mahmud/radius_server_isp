# imports
from django_filters import FilterSet

from .models import Employ


# Employ Filter
class EmployFilter(FilterSet):
 class Meta:
  model = Employ
  fields = ['phone','name']
