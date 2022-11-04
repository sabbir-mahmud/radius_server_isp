# imports
from django.forms import ModelForm

from .models import Owner


# Owner Form
class OwnerForm(ModelForm):
 class Meta:
  model = Owner
  fields = '__all__'