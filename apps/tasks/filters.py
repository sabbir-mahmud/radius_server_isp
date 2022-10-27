# imports
from django_filters import FilterSet

from .models import Tasks


#* task filter
class TaskFilter(FilterSet):
 class Meta:
  model = Tasks
  fields = ['task_token']
