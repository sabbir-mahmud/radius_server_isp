from django.db import models


# pop models
class Pop(models.Model):
 name = models.CharField(max_length=245)
 main_pop = models.ForeignKey('self', on_delete=models.CASCADE,null=True, blank=True)
 input_power = models.IntegerField(null=True, blank=True)
 total_user = models.IntegerField(null=True, blank=True)

 def __str__(self):
  return self.name
