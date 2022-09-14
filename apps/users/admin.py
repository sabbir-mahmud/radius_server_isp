# imports
from django.contrib import admin
# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .forms import UserAdminChangeForm, UserAdminCreationForm
from .models import *

User = get_user_model()

# unregister group model
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
 # The forms to add and change user instances
 form = UserAdminChangeForm
 add_form = UserAdminCreationForm
 # The fields to be used in displaying the User model.
 # These override the definitions on the base UserAdmin
 # that reference specific fields on auth.User.
 list_display = ['email', 'first_name', 'last_name', 'admin']
 list_filter = ['admin']
 fieldsets = (
  (None, {'fields': ('email', 'password')}),
  ('Personal info', {
   'fields': ('first_name', 'last_name', 'gender')}),
   ('Permissions', {'fields': ('staff', 'admin',)}),
 )
 # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
 # overrides get_fieldsets to use this attribute when creating a user.
 add_fieldsets = (
  (None, {
   'classes': ('wide',),
    'fields': ('email', 'password', 'password2', 'first_name', 'last_name', 'gender',  'staff', 'admin')}
   ),
 )
 search_fields = ['email']
 ordering = ['email']
 filter_horizontal = ()

 class Meta:
  model = User
  fields = ['email']

# profile model
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
 list_display = ['user','name','gender']
 list_display_links = ['user','name']
