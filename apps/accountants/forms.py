# imports
from django.forms import ModelForm

from .models import Earning, Invest, Owner


# Owner Form
class OwnerForm(ModelForm):
 class Meta:
  model = Owner
  fields = '__all__'

# invest form
class InvestForm(ModelForm):
 class Meta:
  model = Invest
  fields = '__all__'

# Earning form
class EarningForm(ModelForm):
 class Meta:
  model = Earning
  fields = '__all__'