from secrets import choice
from unicodedata import category

from django.db import models

# * Warehouse Category Model

class WarehouseCategory(models.Model):
 name = models.CharField(max_length=245)

 def __str__(self):
  return self.name

# * warehouse product model

class Warehouse(models.Model):
 choice = (('Active','Active'),('Stored','Stored'),('Damaged','Damaged'))
 Brand = models.CharField(max_length=245)
 model = models.CharField(max_length=245)
 serial = models.CharField(max_length=245)
 category = models.ForeignKey(WarehouseCategory, on_delete=models.CASCADE, null=True, blank=True)
 status = models.CharField(max_length=245, choices=choice)
 created = models.DateTimeField(auto_now_add=True)
 updated = models.DateTimeField(auto_now=True)

 def __str__(self):
  return self.serial
