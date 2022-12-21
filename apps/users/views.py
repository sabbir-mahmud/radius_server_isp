# imports 
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

'''
login user

'''
def loginView(request):
 if request.method == 'POST':
  email = request.POST.get('email')
  password = request.POST.get('password')
  url = request.POST.get('next', '')
  print(url)
  user = authenticate(email=email,password=password)
  if user is not None:
   login(request,user)
   if url:
    return redirect(url)
  else:
   return redirect('dashboard:dashboard')
 return render(request,'auth/login.html')
