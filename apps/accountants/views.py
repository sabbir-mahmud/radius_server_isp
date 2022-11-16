# imports
from datetime import datetime

from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.db.models import Sum
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

from apps.clients.models import Clients

from .filters import EarningFilter, InvestFilter, OwnerFilter
from .forms import (CommissionForm, CompanyProfileForm, EarningForm,
                    InvestForm, OwnerForm)
from .models import Commission, CompanyProfile, Earning, Invest, Owner


# Owner Dashboard
class OwnerDashboard(View):
 def get(self, request):
  # * profit details
  earn = Earning.objects.aggregate(Sum('earning_amount'))['earning_amount__sum'] if Earning.objects.all().exists() else 0
  invest = Invest.objects.aggregate(Sum('invest_amount'))['invest_amount__sum'] if Invest.objects.all().exists() else 0

  def profit_calculator(invest, earn):
    if invest > earn:
      return 0
    else:
      return earn - invest

  # loss calculator
  def loss_calculator(invest, earn):
    if invest < earn:
      return 0
    else:
      return invest - earn
    
  profit = profit_calculator(invest,earn)
  loss = loss_calculator(invest,earn)

  # * billing details
  total_bill = Clients.objects.filter(status='active').aggregate(Sum('pack__price'))['pack__price__sum'] if Clients.objects.filter(status='active').exists() else 0

  commission = Commission.objects.get(id=1)


  earn_via_bill = (total_bill * commission.profit) / 100
  up_steam_bill = total_bill - earn_via_bill

  # * clients details
  clients = Clients.objects.all().count() if Clients.objects.all().exists() else 0
  active_clients = Clients.objects.filter(status='active').count() if Clients.objects.filter(status='active').exists() else 0
  inactive_clients = Clients.objects.filter(status='inactive').count() if Clients.objects.filter(status='inactive').exists() else 0



  context = {
    # * profit details
    'earn':earn,
    'invest':invest,
    'profit':profit,
    'loss':loss,
    'total_bill':total_bill,
    'up_steam_bill':up_steam_bill,
    'earn_via_bill':earn_via_bill,

    # * clients details
    'clients':clients,
    'active_clients':active_clients,
    'inactive_clients':inactive_clients,


  }
  return render(request, 'dashboard/dashboard.html',context)


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

# invest view
class InvestView(View):
  def get(self, request,):
    invests = Invest.objects.all()
    filters = InvestFilter(request.GET, queryset=invests)
    paginator = Paginator(filters.qs, 25)
    page_number = request.GET.get('paginator')
    invests = paginator.get_page(page_number)
    context = {
      'invests':invests, 'filters':filters
    }
    return render(request, 'dashboard/invest/invest.html', context)

# invest create view 
class InvestCreateView(SuccessMessageMixin,CreateView):
  form_class = InvestForm
  template_name = 'dashboard/invest/invest_form.html'
  success_message = 'Invest Details Created'
  error_message = 'Invest Details Not Created'
  success_url = '/dashboard/invest'

# invest update view 
class InvestUpdateView(SuccessMessageMixin,UpdateView):
  model = Invest
  form_class = InvestForm
  template_name = 'dashboard/invest/invest_form.html'
  success_message = 'Invest Details updated'
  error_message = 'Invest Details Not updated'
  success_url = '/dashboard/invest'

# invest delete view
class InvestDelete(SuccessMessageMixin,DeleteView):
  model = Invest
  template_name = 'dashboard/invest/invest_delete_confirm.html'
  success_url = '/dashboard/invest'
  success_message = 'Invests Details Deleted'
  error_message = 'Invests Details Not Deleted'

# * earn view
class EarnView(View):
  def get(self, request,):
    earnings = Earning.objects.all()
    filters = EarningFilter(request.GET, queryset=earnings)
    paginator = Paginator(filters.qs, 25)
    page_number = request.GET.get('paginator')
    earnings = paginator.get_page(page_number)
    context = {
      'earnings':earnings, 'filters':filters
    }
    return render(request, 'dashboard/earnings/earnings.html', context)

# earning create view 
class EarnCreateView(SuccessMessageMixin,CreateView):
  form_class = EarningForm
  template_name = 'dashboard/earnings/earning_form.html'
  success_message = 'Earning Details Created'
  error_message = 'Earning Details Not Created'
  success_url = '/dashboard/earns'

# earn update view 
class EarnUpdateView(SuccessMessageMixin,UpdateView):
  model = Earning
  form_class = EarningForm
  template_name = 'dashboard/earnings/earning_form.html'
  success_message = 'Earning Details updated'
  error_message = 'Earning Details Not updated'
  success_url = '/dashboard/earns'

# earn delete view
class EarnDelete(SuccessMessageMixin,DeleteView):
  model = Earning
  template_name = 'dashboard/earnings/earn_delete_confirm.html'
  success_url = '/dashboard/earns'
  success_message = 'Earning Details Deleted'
  error_message = 'Earning Details Not Deleted'

# Commission Update View
class CommissionUpdateView(SuccessMessageMixin,UpdateView):
  model = Commission
  form_class = CommissionForm
  template_name = 'dashboard/commission/commission_form.html'
  success_url = '/dashboard'
  success_message = 'Commission Details Updated'
  error_message = 'Commission Details Not Updated'


# Company Profile View
class CompanyProfileView(SuccessMessageMixin,UpdateView):
  model = CompanyProfile
  form_class = CompanyProfileForm
  template_name = 'dashboard/profile/profile_form.html'
  success_url = '/dashboard'
  success_message = 'Commission Details Updated'
  error_message = 'Commission Details Not Updated'