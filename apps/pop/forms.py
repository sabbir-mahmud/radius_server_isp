# imports
from django.forms import ModelForm

from .models import Pop


#* PopForm
class PopForm(ModelForm):
 class Meta:
  model = Pop
  fields = '__all__'
