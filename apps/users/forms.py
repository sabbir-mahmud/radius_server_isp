# imports
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# user register form
User = get_user_model()


class RegisterForm(forms.ModelForm):
 # password input
 password = forms.CharField(widget=forms.PasswordInput())
 password2 = forms.CharField(
  widget=forms.PasswordInput(), label='Confirm Password')

 # selecting Model
 class Meta:
  model = User
  fields = [
   'email', 'first_name', 'last_name', 'gender'
  ]

 # password matching and returning password
 def clean(self):
  cleaned_data = super().clean()
  password1 = cleaned_data.get('password')
  password2 = cleaned_data.get('password2')
  if password1 is not None and password1 != password2:
   self.add_error("password2", "Your passwords must match")

  return cleaned_data

 # set password
 def save(self, commit=True):
  user = super(RegisterForm, self).save(commit=False)
  user.set_password(self.cleaned_data['password2'])
  if commit:
   user.save()
  return user

# super user crete form


class UserAdminCreationForm(forms.ModelForm):
 # password input
 password = forms.CharField(widget=forms.PasswordInput())
 password2 = forms.CharField(
  widget=forms.PasswordInput(), label='Confirm Password')

 # selecting Model
 class Meta:
  model = User
  fields = ['email']

 # password matching and returning password
 def clean(self):
  cleaned_data = super().clean()
  password1 = cleaned_data.get('password')
  password2 = cleaned_data.get('password2')
  if password1 is not None and password1 != password2:
   self.add_error("password2", "Your passwords must match")

  return cleaned_data

 # set password
 def save(self, commit=True):
  user = super().save(commit=False)
  user.set_password(self.cleaned_data['password2'])
  if commit:
   user.save()
  return user


# useradminchangeform
class UserAdminChangeForm(forms.ModelForm):
 password = ReadOnlyPasswordHashField()

 class Meta:
  model = User
  fields = ['email', 'password', 'admin']

 def clean_password(self):
  # Regardless of what the user provides, return the initial value.
  # This is done here, rather than on the field, because the
  # field does not have access to the initial value
  return self.initial["password"]
