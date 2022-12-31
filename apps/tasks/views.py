# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.db.models import Sum
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

from .filters import TaskFilter
from .forms import TaskCategoryForm, TasksForm
from .models import TaskCategory, Tasks

# Create your views here.

# Task lists
@method_decorator(login_required(login_url='login'), name='dispatch')
class TasksView(View):
 def get(self,request):
  tasks = Tasks.objects.all()
  filters = TaskFilter(request.GET, queryset=tasks)
  tasks = filters.qs
  paginator = Paginator(tasks, 25)
  page_number = request.GET.get('paginator')
  tasks = paginator.get_page(page_number)
  context = {
   'tasks':tasks,'filters':filters
  }
  return render(request, 'tasks/tasks.html', context)


# tasks Create view
@login_required(login_url='login')
def createTasks(request):  
  form = TasksForm()
  if request.method == 'POST':
    form = TasksForm(request.POST)
    if form.is_valid():
      obj = form.save(commit=False)
      task_id = Tasks.objects.aggregate(Sum('task_token'))['task_token__sum'] + 1 if Tasks.objects.aggregate(Sum('task_token'))['task_token__sum'] else 100000 
      obj.task_token = task_id
      obj.save()
      return redirect('tasks:tasks')

  context = {
    'form':form
  }
  return render(request,'tasks/task_form.html',context)

# tasks Update View
@method_decorator(login_required(login_url='login'), name='dispatch')
class UpdateTasks(SuccessMessageMixin,UpdateView):
 model = Tasks
 form_class = TasksForm
 template_name = 'tasks/task_form.html'
 success_url = '/tasks'
 success_message ='new tasks updated'
 error_message ='tasks not updated'


# tasks Delete View
@method_decorator(login_required(login_url='login'), name='dispatch')
class DeleteTasks(SuccessMessageMixin,DeleteView):
  model = Tasks
  template_name = 'tasks/tasks_delete.html'
  success_url = '/tasks'
  success_message ='tasks deleted'
  error_message ='tasks not deleted'


# Task category lists
@method_decorator(login_required(login_url='login'), name='dispatch')
class TasksCategoryView(View):
 def get(self,request):
  taskCategory = TaskCategory.objects.all()
  filters = TaskFilter(request.GET, queryset=taskCategory)
  taskCategory = filters.qs
  paginator = Paginator(taskCategory, 25)
  page_number = request.GET.get('paginator')
  taskCategory = paginator.get_page(page_number)
  context = {
   'taskCategory':taskCategory,'filters':filters
  }
  return render(request, 'taskCategory/taskCategory.html', context)


# tasks Create view
@method_decorator(login_required(login_url='login'), name='dispatch')
class CreateTasksCategory(SuccessMessageMixin,CreateView):  
  form_class = TaskCategoryForm
  template_name = 'taskCategory/tasksCategory_form.html'
  success_url = '/tasks/taskCategory'
  success_message ='task category created'
  error_message ='task category not created'

# tasks Update View
@method_decorator(login_required(login_url='login'), name='dispatch')
class UpdateTasksCategory(SuccessMessageMixin,UpdateView):
  model= TaskCategory
  form_class = TaskCategoryForm
  template_name = 'taskCategory/tasksCategory_form.html'
  success_url = '/tasks/taskCategory'
  success_message ='task category updated'
  error_message ='task category not updated'


# tasks Delete View
@method_decorator(login_required(login_url='login'), name='dispatch')
class DeleteTasksCategory(SuccessMessageMixin,DeleteView):
  model = TaskCategory
  template_name = 'taskCategory/tasksCategory_delete.html'
  success_url = '/tasks/taskCategory'
  success_message ='task category deleted'
  error_message ='task category not deleted'
