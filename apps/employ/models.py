from django.contrib.auth import get_user_model
from django.db import models

# user
User = get_user_model()


# Worker category model

class EmployCategory(models.Model):
 name = models.CharField(max_length=245)

 def __str__(self):
  return self.name


# Employ models

class Employ(models.Model):
 choices_select = (('active', 'active'), ('inactive', 'inactive'))
 user = models.OneToOneField(User, on_delete=models.CASCADE)
 name = models.CharField(max_length=100)
 father_name = models.CharField(max_length=245)
 mother_name = models.CharField(max_length=245)
 email = models.EmailField(max_length=100)
 phone = models.CharField(max_length=100, verbose_name='phone')
 nid = models.CharField(max_length=100)
 address = models.CharField(max_length=100)
 status = models.CharField(max_length=50, choices=choices_select, default='active')
 type = models.ForeignKey(EmployCategory, on_delete=models.CASCADE)
 created = models.DateTimeField(auto_now_add=True)
 updated = models.DateTimeField(auto_now=True)

 def __str__(self):
  return self.name
