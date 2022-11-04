# imports
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

from .filters import OwnerFilter
from .forms import OwnerForm
from .models import Owner


# Owner Dashboard
class OwnerDashboard(View):
 def get(self, request):
  return render(request, 'dashboard/baseDashboard.html')


# owners view
class OwnerView(View):
 def get(self, request):
  owners = Owner.objects.all()
  filters = OwnerFilter(request.GET, queryset=owners)
  paginator = Paginator(filters.qs, 7)
  page_number = request.GET.get('paginator')
  owners = paginator.get_page(page_number)
  context = {
   'owners':owners, 'filters':filters
  }
  return render(request, 'dashboard/owner/owner.html', context)

# owner create view
class OwnerCreate(SuccessMessageMixin,CreateView):
 form_class = OwnerForm
 template_name = 'dashboard/owner/owner_form.html'
 success_url = '/dashboard/owners'
 success_message = 'owner created'
 error_message = 'owner not created'

# owner update view
class OwnerUpdate(SuccessMessageMixin,UpdateView):
 model = Owner
 form_class = OwnerForm
 template_name = 'dashboard/owner/owner_form.html'
 success_url = '/dashboard/owners'
 success_message = 'owner updated'
 error_message = 'owner not updated'

# owner delete view
class OwnerDelete(SuccessMessageMixin,DeleteView):
 model = Owner
 template_name = 'dashboard/owner/owner_delete_confirm.html'
 success_url = '/dashboard/owners'
 success_message = 'owner deleted'
 error_message = 'owner not deleted'
