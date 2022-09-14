from secrets import choice

from django.db import models

# Create your models here.
# Warehouse Category Model

class WarehouseCategory(models.Model):
 name = models.CharField(max_length=245)

 def __str__(self):
  return self.name

class Warehouse(models.Model):
 choice = (('Active','Active'),('Stored','Stored'),('Damaged','Damaged'))
 Brand = models.CharField(max_length=245)
 model = models.CharField(max_length=245)
 serial = models.CharField(max_length=245)
 status = models.CharField(max_length=245, choices=choice)
 created = models.DateTimeField(auto_now_add=True)
 updated = models.DateTimeField(auto_now=True)
 price = models.FloatField()

 def __str__(self):
  return self.serial
