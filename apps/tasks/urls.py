# imports
from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
 path('', views.TasksView.as_view(), name='tasks'),
 path('create/', views.createTasks, name='create'),
 path('update/<str:pk>/', views.UpdateTasks.as_view(), name='update'),
 path('delete/<str:pk>/', views.DeleteTasks.as_view(), name='delete'),
 path('taskCategory/', views.TasksCategoryView.as_view(), name='tasks-category'),
 path('taskCategory/create/', views.CreateTasksCategory.as_view(), name='create-category'),
 path('taskCategory/update/<str:pk>/', views.UpdateTasksCategory.as_view(), name='update-category'),
 path('taskCategory/delete/<str:pk>/', views.DeleteTasksCategory.as_view(), name='delete-category'),
]
