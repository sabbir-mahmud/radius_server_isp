# imports
from django.urls import path

from . import views

urlpatterns = [
     path('',views.loginView, name='login'),
     path('users',views.UsersView.as_view(), name='user'),
     path('users/<str:pk>',views.UpdateUser.as_view(), name='user-update'),
     path('users/del/<str:pk>',views.delete_user, name='user-delete'),
     path("logout/", views.logoutView, name="logout"),
     path("create/", views.register, name="create-user"),
     path("profile/", views.ProfileView.as_view(), name="profile"),
]