# imports 
from django import forms

from .models import Clients


# Clients Forms
class ClientsForm(forms.ModelForm):
 class Meta:
  model = Clients
  fields = '__all__'
