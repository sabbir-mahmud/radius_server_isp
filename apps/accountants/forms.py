# imports
from django.forms import ModelForm

from .models import Commission, CompanyProfile, Earning, Invest, Owner


# Company Profile Form
class CompanyProfileForm(ModelForm):
  class Meta:
    model = CompanyProfile
    fields = '__all__'

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

# Commission form
class CommissionForm(ModelForm):
  class Meta:
    model = Commission
    fields = '__all__'