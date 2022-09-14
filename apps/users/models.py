# imports
import pathlib

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


# user manager
class UserManager(BaseUserManager):
 # create user
 def create_user(self, email, password=None):
  if not email:
   raise ValueError('Enter a valid email')

  user = self.model(email=self.normalize_email(email))
  user.set_password(password)
  user.save(using=self._db)
  return user

 # create staff user
 def create_staffuser(self, email, password=None):
  user = self.create_user(email, password)
  user.staff = True
  user.save(using=self._db)
  return user

 # create super user / admin
 def create_superuser(self, email, password=None):
  user = self.create_user(email, password)
  user.staff = True
  user.admin = True
  user.save(using=self._db)
  return user

# user model
class User(AbstractBaseUser):
 email = models.EmailField(max_length=245, unique=True)
 first_name = models.CharField(max_length=245)
 last_name = models.CharField(max_length=245)
 gender = models.CharField(max_length=245)
 owner = models.BooleanField(default=False)
 employs = models.BooleanField(default=False)
 staff = models.BooleanField(default=False)
 admin = models.BooleanField(default=False)
 created = models.DateTimeField(auto_now_add=True)
 updated = models.DateTimeField(auto_now=True)

 # username replaced with email
 USERNAME_FIELD = 'email'
 REQUIRED_FIELDS = []

 objects = UserManager()

 def __str__(self):
  return self.email

 def has_perm(self, perm, obj=None):
  return True

 def has_module_perms(self, app_label):
  return True

 @property
 def is_staff(self):
  if self.staff == True:
   return True
  else:
   return False

 @property
 def is_superuser(self):
  if self.admin == True:
   return True
  else:
   return False


# img rename
def img_uploader(instance,filename):
  fpath = pathlib.Path(filename)
  new_fname = str(instance.user)
  return f'profiles_img/{new_fname}{fpath.suffix}'

# Profile Model
class Profile(models.Model):
 user = models.OneToOneField(User, on_delete=models.CASCADE)
 name = models.CharField(max_length=245)
 gender = models.CharField(max_length=10)
 img = models.ImageField(upload_to=img_uploader, null=True, blank=True)
 bio = models.CharField(max_length=245, null=True, blank=True)
 created = models.DateTimeField(auto_now_add=True)
 updated = models.DateTimeField(auto_now=True)

 def __str__(self):
  return self.name

 class Meta:
  verbose_name = 'Profile'
  verbose_name_plural = 'Profiles'
  ordering = ['-id']
