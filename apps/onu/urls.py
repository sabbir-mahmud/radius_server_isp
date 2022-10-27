# imports
from django.urls import path

from . import views

app_name = 'onu'

urlpatterns = [
 path('', views.OnuList.as_view(), name='onus'),
 path('create', views.OnuCreate.as_view(), name='create'),
 path('update/<str:pk>', views.OnuUpdate.as_view(), name='update'),
 path('delete/<str:pk>', views.OnuDelete.as_view(), name='delete'),
 ]
