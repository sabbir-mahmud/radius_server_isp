# imports
from django.urls import path

from apps.employ import views as employ_views

from . import views

app_name = 'dashboard'

urlpatterns = [
 path('', views.OwnerDashboard.as_view(), name='dashboard'),
 path('employ', employ_views.EmployView.as_view(), name='employ'),
 path('employ/create', employ_views.EmployCreate.as_view(), name='employ-create'),
 path('employ/update/<str:pk>', employ_views.UpdateEmploy.as_view(), name='employ-update'),
 path('employ/delete/<str:pk>', employ_views.EmployDelete.as_view(), name='employ-delete'),
 
]
