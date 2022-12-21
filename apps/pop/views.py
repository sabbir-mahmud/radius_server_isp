# imports
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

from .filters import PopFilter
from .forms import PopForm
from .models import Pop

'''
Pop list view

'''
@method_decorator(login_required(login_url='login'), name='dispatch')
class PopList(View):
 def get(self, request):
  pops = Pop.objects.all()
  filters = PopFilter(request.GET, queryset=pops)
  paginator = Paginator(filters.qs, 25)
  page_number = request.GET.get('page_number')
  pops = paginator.get_page(page_number)

  context = {
   'pops':pops, 'filters':filters
  }

  return render(request,'pop/pops.html', context)


'''
Pop Create View

'''
@method_decorator(login_required(login_url='login'), name='dispatch')
class CreatePop(SuccessMessageMixin,CreateView):
 form_class = PopForm
 template_name = 'pop/pop_form.html'
 success_url = '/pops'
 success_message = 'pop created'
 error_message = 'failed to create pop'


'''
Pop Update View

'''
@method_decorator(login_required(login_url='login'), name='dispatch')
class UpdatePop(SuccessMessageMixin,UpdateView):
 model = Pop
 form_class = PopForm
 template_name = 'pop/pop_form.html'
 success_url = '/pops'
 success_message = 'pop created'
 error_message = 'failed to create pop'


'''
Pop Delete View

'''
@method_decorator(login_required(login_url='login'), name='dispatch')
class DeletePop(SuccessMessageMixin,DeleteView):
 model = Pop
 template_name = 'pop/pop_delete_form.html'
 success_url = '/pops'
 success_message = 'pop created'
 error_message = 'failed to create pop'
