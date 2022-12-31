# imports 
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .decorator import auth_user

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
