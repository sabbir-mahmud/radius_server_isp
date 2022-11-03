# imports
from django.urls import path

from apps.employ import views as employ_views

from . import views

app_name = 'dashboard'

urlpatterns = [
 path('', views.OwnerDashboard.as_view(), name='dashboard'),
 # ? employ urls
 path('employ', employ_views.EmployView.as_view(), name='employ'),
 path('employ/create', employ_views.EmployCreate.as_view(), name='employ-create'),
 path('employ/update/<str:pk>', employ_views.UpdateEmploy.as_view(), name='employ-update'),
 path('employ/delete/<str:pk>', employ_views.EmployDelete.as_view(), name='employ-delete'),
 path('employ/category', employ_views.EmployCategoryView.as_view(), name='employ_category'),
 path('employ/category/create', employ_views.EmployCategoryCreate.as_view(), name='employ_category-create'),
 path('employ/category/update/<str:pk>', employ_views.UpdateCategoryEmploy.as_view(), name='employ_category-update'),
 path('employ/category/delete/<str:pk>', employ_views.EmployCategoryDelete.as_view(), name='employ_category-delete'),
 
]
