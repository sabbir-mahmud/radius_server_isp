from django.db import models


# Create your models here.
# pop models
class Pop(models.Model):
 name = models.CharField(max_length=245)
 main_pop = models.ForeignKey('self', on_delete=models.CASCADE)

 def __str__(self):
  return self.name
