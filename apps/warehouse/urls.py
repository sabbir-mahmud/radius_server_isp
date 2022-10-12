# imports
from django.urls import path

from . import views

app_name = 'warehouse'

urlpatterns = [
 path('', views.WarehouseProductList.as_view(), name='warehouse'),
 path('create', views.WarehouseProductCreate.as_view(), name='warehouse-create'),
 path('update/<str:pk>', views.WarehouseProductUpdate.as_view(), name='warehouse-update'),
 path('delete/<str:pk>', views.WarehouseProductDelete.as_view(), name='warehouse-delete'),


 path('categories', views.WarehouseCategoryList.as_view(),name='category'),
 path('categories/create', views.WarehouseCreateCategory.as_view(),name='category-create'),
 path('categories/update/<str:pk>', views.WarehouseUpdateCategory.as_view(),name='category-update'),
 path('categories/delete/<str:pk>', views.WarehouseDeleteCategory.as_view(),name='category-delete'),

 
]
