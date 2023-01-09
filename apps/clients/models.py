from enum import unique

from django.db import models

from apps.onu.models import Onu
from apps.packages.models import Package
from apps.pop.models import Pop

# clients models
# internet user model

class Clients(models.Model):
 choices_select = (('active', 'active'), ('inactive', 'inactive'))
 name = models.CharField(max_length=100)
 email = models.EmailField(max_length=100)
 client_id = models.IntegerField(unique=True)
 phone = models.CharField(max_length=100, verbose_name='phone')
 nid = models.CharField(max_length=100)
 address = models.CharField(max_length=100)
 ip = models.CharField(max_length=100, unique=True,verbose_name='IP/UserName')
 pack = models.ForeignKey(Package, on_delete=models.CASCADE)
 onu = models.ForeignKey(Onu, on_delete=models.CASCADE)
 status = models.CharField(max_length=50, choices=choices_select, default='inactive')
 pop_name = models.ForeignKey(Pop, on_delete=models.CASCADE)
 created = models.DateTimeField(auto_now_add=True)
 updated = models.DateTimeField(auto_now=True)

 def __str__(self):
  return self.name
