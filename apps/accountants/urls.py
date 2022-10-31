# imports
from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
 path('', views.OwnerDashboard.as_view(), name='dashboard'),
 
]
