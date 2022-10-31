# imports
from django.shortcuts import render
from django.views import View

from .models import Owner


# Owner Dashboard
class OwnerDashboard(View):
 def get(self, request):
  return render(request, 'dashboard/baseDashboard.html')
