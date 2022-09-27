from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

from .forms import ClientsForm
from .models import Clients

# Create your views here.

# Clients Models
class ClientsView(View):
 def get(self,request):
  clients = Clients.objects.all()
  context = {
   'clients':clients
  }
  return render(request, 'clients/clients.html', context)


# Clients Create view
class CreateClients(SuccessMessageMixin,CreateView):
 form_class = ClientsForm
 template_name = 'clients/create_client.html'
 success_url = '/clients'
 success_message ='new clients created'
 error_message ='clients not created'
 

# clients Update View
class UpdateClients(SuccessMessageMixin,UpdateView):
 model = Clients
 form_class = ClientsForm
 template_name = 'clients/create_client.html'
 success_url = '/clients'
 success_message ='new clients updated'
 error_message ='clients not updated'
