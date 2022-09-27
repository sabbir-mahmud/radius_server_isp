# imports
from django.urls import path

from . import views

app_name = 'client'

urlpatterns = [
 path('', views.ClientsView.as_view(), name='clients'),
 path('create/', views.CreateClients.as_view(), name='create'),
 path('update/<str:pk>/', views.UpdateClients.as_view(), name='update'),
]
