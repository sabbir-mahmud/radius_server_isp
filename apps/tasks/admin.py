# imports
from django.contrib import admin

from .models import TaskCategory, Tasks

# Register your models here.
admin.site.register(TaskCategory)
admin.site.register(Tasks)
