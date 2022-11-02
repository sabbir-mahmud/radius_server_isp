# imports
from django.forms import ModelForm

from .models import Employ, EmployCategory


# Employ Category Form
class EmployCategoryForm(ModelForm):
 class Meta:
  model = EmployCategory
  fields = '__all__'

 
# Employ Form
class EmployForm(ModelForm):
 class Meta:
  model = Employ
  fields = '__all__'
