# imports
from django.db import models


#* Onu Models
class Onu(models.Model):
 choice = (('Active','Active'),('Stored','Stored'),('Damaged','Damaged'))
 brand = models.CharField(max_length=245)
 model = models.CharField(max_length=245)
 mac = models.CharField(max_length=245)
 port = models.IntegerField()
 status = models.CharField(max_length=10, choices=choice)
 created = models.DateTimeField(auto_now_add=True)
 updated = models.DateTimeField(auto_now=True)

 def __str__(self):
  return self.mac
