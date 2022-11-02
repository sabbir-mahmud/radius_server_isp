# imports
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

from .filters import EmployFilter
from .forms import EmployCategoryForm, EmployForm
from .models import Employ, EmployCategory


# Employ Management panel
class EmployView(View):
 def get(self, request):
  employs = Employ.objects.all()
  filters = EmployFilter(request.GET, queryset=employs)
  employs = filters.qs
  paginator = Paginator(employs, 25)
  page_number = request.GET.get('paginator')
  employs = paginator.get_page(page_number)
  context = {
   'employs':employs,'filters':filters
  }
  return render(request, 'dashboard/employ/employ.html', context)

# Employ Create View
class EmployCreate(SuccessMessageMixin,CreateView):
 form_class = EmployForm
 template_name = 'dashboard/employ/employ_form.html'
 success_url = '/dashboard/employ'
 success_message = 'Employ created'
 error_message = 'Employ not created'


# Employ Update View
class UpdateEmploy(SuccessMessageMixin,UpdateView):
 model = Employ
 form_class = EmployForm
 template_name = 'dashboard/employ/employ_form.html'
 success_url = '/dashboard/employ'
 success_message = 'Employ updated'
 error_message = 'Employ not updated'

# Employ Delete View
class EmployDelete(SuccessMessageMixin,DeleteView):
 model = Employ
 template_name = 'dashboard/employ/employ_delete_confirm.html'
 success_url = '/dashboard/employ'
 success_message = 'Employ deleted'
 error_message = 'Employ not deleted'
