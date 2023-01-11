# imports
from django.urls import include, path

from . import views

app_name = 'packages'

urlpatterns = [
    path('',views.PackagesView.as_view(), name='packages'),
    path('create/',views.PackagesCreateView.as_view(), name='create'),
    path('update/<str:pk>',views.PackagesUpdateView.as_view(), name='update'),
    path('delete/<str:pk>',views.DeletePackages.as_view(), name='delete'),

]