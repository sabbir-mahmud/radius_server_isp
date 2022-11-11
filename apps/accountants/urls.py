# imports
from django.urls import path

from apps.employ import views as employ_views

from . import views

app_name = 'dashboard'

urlpatterns = [
 path('', views.OwnerDashboard.as_view(), name='dashboard'),
 # ? owners urls
 path('owners', views.OwnerView.as_view(), name='owners'),
 path('owners/create', views.OwnerCreate.as_view(), name='owner-create'),
 path('owners/update/<str:pk>', views.OwnerUpdate.as_view(), name='owner-update'),
 path('owners/delete/<str:pk>', views.OwnerDelete.as_view(), name='owner-delete'),
 # ? employ urls
 path('employ', employ_views.EmployView.as_view(), name='employ'),
 path('employ/create', employ_views.EmployCreate.as_view(), name='employ-create'),
 path('employ/update/<str:pk>', employ_views.UpdateEmploy.as_view(), name='employ-update'),
 path('employ/delete/<str:pk>', employ_views.EmployDelete.as_view(), name='employ-delete'),
 path('employ/category', employ_views.EmployCategoryView.as_view(), name='employ_category'),
 path('employ/category/create', employ_views.EmployCategoryCreate.as_view(), name='employ_category-create'),
 path('employ/category/update/<str:pk>', employ_views.UpdateCategoryEmploy.as_view(), name='employ_category-update'),
 path('employ/category/delete/<str:pk>', employ_views.EmployCategoryDelete.as_view(), name='employ_category-delete'),

 # ? invests urls
 path('invest/', views.InvestView.as_view(), name='invests'),
 path('invest/create', views.InvestCreateView.as_view(), name='invests-create'),
 path('invest/update/<str:pk>/', views.InvestUpdateView.as_view(), name='invests-update'),
 path('invest/delete/<str:pk>/', views.InvestDelete.as_view(), name='invests-delete'),

 # ? invests urls
 path('earns/', views.EarnView.as_view(), name='earns'),
 path('earns/create', views.EarnCreateView.as_view(), name='earns-create'),
 path('earns/update/<str:pk>/', views.EarnUpdateView.as_view(), name='earns-update'),
 path('earns/delete/<str:pk>/', views.EarnDelete.as_view(), name='earns-delete'),

 # ? commissions update urls
 path('settings/commission/update/<str:pk>',views.CommissionUpdateView.as_view(), name='commission-update'),

 # ? profile update urls
 path('settings/profile/update/<str:pk>',views.CompanyProfileView.as_view(), name='profile-update')
 
]
