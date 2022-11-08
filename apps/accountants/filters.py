# imports
from django_filters import FilterSet

from .models import Earning, Invest, Owner


# owner filters
class OwnerFilter(FilterSet):
 class Meta:
  model = Owner
  fields = ['name']

# invest filters
class InvestFilter(FilterSet):
 class Meta:
  model = Invest
  fields = ['created_at']

# Earning filters
class EarningFilter(FilterSet):
 class Meta:
  model = Earning
  fields = ['created_at']