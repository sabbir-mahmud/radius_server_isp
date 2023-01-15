# imports 
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.views.generic import UpdateView, View

from .decorator import auth_user
from .forms import RegisterForm, UserUpdateForm
from .models import Profile

'''
User Model

'''
User = get_user_model()

class UsersView(View):
  def get(self, request):
    users = User.objects.all()
    context = {
      'users':users
    }
    return render(request, 'auth/users.html', context)


'''
Create User

'''
def register(request):
  form = RegisterForm()
  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('user')
  context = {'form':form}
  return render(request,'auth/createUser.html',context)

'''
Update User

'''
class UpdateUser(SuccessMessageMixin, UpdateView):
  model = User
  template_name = 'auth/user_form.html'
  form_class = UserUpdateForm
  success_url = '/users'
  success_message = 'User updated successfully'
  error_message = 'User not updated'

'''
Delete User

'''
def delete_user(request,pk):
  User.objects.get(id=pk).delete()
  return redirect('user')


'''
login user

'''
@auth_user
def loginView(request):
  if request.method == 'POST':
    email = request.POST.get('email')
    password = request.POST.get('password')
  
    user = authenticate(email=email,password=password)
    if user is not None:
      login(request,user)
      if "next" in request.POST:
        return redirect(request.POST['next']) 
      return redirect('dashboard:dashboard')
  return render(request,'auth/login.html')


'''
log out user

'''
def logoutView(request):
  logout(request)
  return redirect('/')

'''
profile view

'''
class ProfileView(View):
  def get(self,request):
    user = request.user.id
    user_data = Profile.objects.get(user=user)
    context = {
      'user_data':user_data
    }
    return render(request, 'users/profile.html',context)
