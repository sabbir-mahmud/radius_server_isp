# imports

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from .models import Profile

# user model
User = get_user_model()



# profile signals
def create_profile(created, instance,*args, **kwargs):
 if created:
  Profile.objects.create(
   user=instance,
   name=f'{instance.first_name} {instance.last_name}',
   gender=instance.gender,
  )





post_save.connect(create_profile, sender=User)
