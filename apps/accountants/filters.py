# imports
from django_filters import FilterSet

from .models import Owner


# owner filters
class OwnerFilter(FilterSet):
 class Meta:
  model = Owner
  fields = ['name']