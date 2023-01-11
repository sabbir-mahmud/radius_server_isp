# imports
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.db.models import Sum
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

from .filters import ClientFilter
from .forms import ClientsForm
from .models import Clients

# Create your views here.

# Clients Models
@method_decorator(login_required(login_url='login'), name='dispatch')
class ClientsView(View):
 def get(self,request):
  clients = Clients.objects.all()
  filters = ClientFilter(request.GET, queryset=clients)
  clients = filters.qs
  paginator = Paginator(clients, 25)
  page_number = request.GET.get('paginator')
  clients = paginator.get_page(page_number)
  context = {
   'clients':clients,'filters':filters
  }
  return render(request, 'clients/clients.html', context)


# Clients Create view
@login_required(login_url='login')
def createClients(request):  
  form = ClientsForm()
  if request.method == 'POST':
    form = ClientsForm(request.POST)
    if form.is_valid():
      obj = form.save(commit=False)
      c_id = Clients.objects.aggregate(Sum('client_id'))['client_id__sum'] + 1 if Clients.objects.aggregate(Sum('client_id'))['client_id__sum'] else 100000 
      obj.client_id = c_id
      obj.save()
      return redirect('client:clients')

  context = {
    'form':form
  }
  return render(request,'clients/create_client.html',context)

# clients Update View
@method_decorator(login_required(login_url='login'), name='dispatch')
class UpdateClients(SuccessMessageMixin,UpdateView):
 model = Clients
 form_class = ClientsForm
 template_name = 'clients/create_client.html'
 success_url = '/clients'
 success_message ='new clients updated'
 error_message ='clients not updated'


# clients Delete View
@method_decorator(login_required(login_url='login'), name='dispatch')
class DeleteClients(SuccessMessageMixin,DeleteView):
  model = Clients
  template_name = 'clients/clients_delete.html'
  success_url = '/clients'
  success_message ='clients deleted'
  error_message ='clients not deleted'
