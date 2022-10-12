# imports
from django.urls import path

from . import views

app_name = 'client'

urlpatterns = [
 path('', views.ClientsView.as_view(), name='clients'),
 path('create/', views.createClients, name='create'),
 path('update/<str:pk>/', views.UpdateClients.as_view(), name='update'),
 path('delete/<str:pk>/', views.DeleteClients.as_view(), name='delete'),
]
