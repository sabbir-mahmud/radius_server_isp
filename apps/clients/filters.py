# imports
from django_filters import FilterSet

from .models import Clients


# clients filter
class ClientFilter(FilterSet):
 class Meta:
  model = Clients
  fields = ['phone','ip']
