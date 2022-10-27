# Imports
from django.db import models

from apps.employ.models import Employ


#* Task category Model
class TaskCategory(models.Model):
 name = models.CharField(max_length=150)

 def __str__(self):
  return self.name

# * Task Model
class Tasks(models.Model):
 status = (('pending','pending'),('in progress', 'in progress'),('complete','complete'))
 title = models.CharField(max_length=150)
 task_category = models.ForeignKey(TaskCategory, on_delete=models.CASCADE)
 describe = models.TextField()
 equipment_price = models.IntegerField(null=True, blank=True)
 client_charged = models.IntegerField(null=True, blank=True)
 traveling_allowance = models.IntegerField(null=True, blank=True)
 creator = models.ForeignKey(Employ, on_delete=models.CASCADE, related_name = 'Task_Creator')
 solver = models.ForeignKey(Employ, on_delete=models.CASCADE, null=True, blank=True)
 task_token = models.IntegerField()
 status = models.CharField(max_length=150, choices=status)
 approved = models.BooleanField(default=False)
 created = models.DateTimeField(auto_now_add=True)
 updated = models.DateTimeField(auto_now=True)

 def __str__(self):
  return self.title



