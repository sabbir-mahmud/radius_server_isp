# imports
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.db.models import Sum
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

from .filters import OnuFilter
from .forms import OnuForm
from .models import Onu


#* onu lists
class OnuList(View):
 def get(self, request):
  onus = Onu.objects.all()
  filters = OnuFilter(request.GET, queryset =onus)
  onus = filters.qs
  paginator = Paginator(onus, 25)
  page_number = request.GET.get('paginator')
  onus = paginator.get_page(page_number)
  context = {
   'onus':onus, 'filters':filters
  }
  return render(request,'onu/onus.html', context)

#* Onu create
class OnuCreate(SuccessMessageMixin, CreateView):
 form_class = OnuForm
 template_name = 'onu/onu_form.html'
 success_url = '/onus'
 success_message = 'onu created'
 error_message = 'failed to created onu'


#* Onu Update
class OnuUpdate(SuccessMessageMixin, UpdateView):
 model = Onu
 form_class = OnuForm
 template_name = 'onu/onu_form.html'
 success_url = '/onus'
 success_message = 'onu updated'
 error_message = 'failed to updated onu'


#* Onu Delete
class OnuDelete(SuccessMessageMixin,DeleteView):
 model = Onu
 template_name = 'onu/onu_delete_form.html'
 success_url = '/onus'
 success_message = 'onu deleted'
 error_message = 'failed to deleted onu'