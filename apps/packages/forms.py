# imports 
from django import forms

from .models import Package


# Clients Forms
class PackagesForm(forms.ModelForm):
 class Meta:
  model = Package
  fields = '__all__'