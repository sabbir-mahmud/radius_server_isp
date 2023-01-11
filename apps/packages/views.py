# imports
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

from .forms import PackagesForm
from .models import Package


# Packages list view
@method_decorator(login_required(login_url='login'), name='dispatch')
class PackagesView(View):
    def get(self,request):
        packages = Package.objects.all()
        context = {
            'packages':packages
        }
        return render(request, 'packages/packages.html', context)

# Packages Create view
@method_decorator(login_required(login_url='login'), name='dispatch')
class PackagesCreateView(SuccessMessageMixin,CreateView):
 form_class = PackagesForm
 template_name = 'packages/packages_form.html'
 success_url = '/packages'
 success_message ='new packages created'
 error_message ='packages not created'


# Packages Update view
class PackagesUpdateView(SuccessMessageMixin,UpdateView):
   model = Package
   form_class = PackagesForm
   template_name = 'packages/packages_form.html'
   success_url = '/packages'
   success_message ='packages updated'
   error_message ='packages not updated'

# clients Delete View
@method_decorator(login_required(login_url='login'), name='dispatch')
class DeletePackages(SuccessMessageMixin,DeleteView):
  model = Package
  template_name = 'packages/packages_delete.html'
  success_url = '/packages'
  success_message ='packages deleted'
  error_message ='packages not deleted'