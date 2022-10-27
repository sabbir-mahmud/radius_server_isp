# imports
from dataclasses import field

from django.forms import ModelForm

from .models import TaskCategory, Tasks


#* Task Category Form
class TaskCategoryForm(ModelForm):
 class Meta:
  model = TaskCategory
  fields = '__all__'


#* Tasks Form
class TasksForm(ModelForm):
 class Meta:
  model = Tasks
  fields = '__all__'
  exclude = ['task_token']
