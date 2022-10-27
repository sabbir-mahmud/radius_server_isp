# imports
from django.urls import path

from . import views

app_name = 'pop'

urlpatterns = [
 path('', views.PopList.as_view(), name='pop'),
 path('create', views.CreatePop.as_view(), name='create'),
 path('update/<str:pk>', views.UpdatePop.as_view(), name='update'),
 path('delete/<str:pk>', views.DeletePop.as_view(), name='delete'),
 ]
