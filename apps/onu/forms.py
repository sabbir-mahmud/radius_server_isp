# imports
from django.forms import ModelForm

from .models import Onu


#* Onu Form
class OnuForm(ModelForm):
 class Meta:
  model = Onu
  fields = '__all__'
