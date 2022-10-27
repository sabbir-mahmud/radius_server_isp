# imports
from django.contrib.auth import get_user_model
from django.db import models

# user
User = get_user_model()

# owner model
class Owner(models.Model):
 user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Owner')
 name = models.CharField(max_length=150)
 Commission = models.IntegerField()

 def __str__(self):
  return self.name

# model wrapper
class Wrapper(models.Model):
 created_at = models.DateTimeField(auto_now_add=True)
 created_at = models.DateTimeField(auto_now=True)


# invest model
class Invest(Wrapper):
 invest_details = models.CharField(max_length=500)
 invest_amount = models.IntegerField()

 def __str__(self):
  return self.invest_details


# earning model
class Earning(Wrapper):
 earning_details = models.CharField(max_length=500)
 earning_amount = models.IntegerField()

 def __str__(self):
  return self.earning_details

# Commission model
class Commission(models.Model):
 profit = models.IntegerField()

 def __str__(self):
  return str(self.profit)
