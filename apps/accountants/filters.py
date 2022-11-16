# imports
import django_filters

from .models import Earning, Invest, Owner


# owner filters
class OwnerFilter(django_filters.FilterSet):
 class Meta:
  model = Owner
  fields = ['name']

# invest filters
class InvestFilter(django_filters.FilterSet):
 created_at = django_filters.DateTimeFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type':'date'}))
 class Meta:
  model = Invest
  fields = []

# Earning filters
class EarningFilter(django_filters.FilterSet):
 class Meta:
  model = Earning
  fields = ['created_at']