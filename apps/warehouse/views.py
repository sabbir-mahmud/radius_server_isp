from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

from .filters import CategoryFilter, WarehouseFilter
from .forms import WarehouseCategoryForm, WarehouseProductForm
from .models import Warehouse, WarehouseCategory

# warehouse category 
# warehouse category list

class WarehouseCategoryList(View):
 def get(self,request):
  categories = WarehouseCategory.objects.all()
  filters = CategoryFilter(request.GET, queryset=categories)
  categories = filters.qs
  paginator = Paginator(categories, 25)
  page_number = request.GET.get('paginator')
  categories = paginator.get_page(page_number)
  context = {
   'categories':categories, 'filters':filters
  }
  return render(request, 'warehouse/category.html', context)

# create warehouse category
class WarehouseCreateCategory(SuccessMessageMixin, CreateView):
 form_class = WarehouseCategoryForm
 template_name = 'warehouse/create_category.html'
 success_url = '/warehouse/categories'
 success_message = 'category created'
 error_message = 'failed category creating'

# update warehouse category
class WarehouseUpdateCategory(SuccessMessageMixin, UpdateView):
 model = WarehouseCategory
 form_class = WarehouseCategoryForm
 template_name = 'warehouse/create_category.html'
 success_url = '/warehouse/categories'
 success_message = 'category updated'
 error_message = 'failed category updating'

# delete warehouse category
class WarehouseDeleteCategory(SuccessMessageMixin,DeleteView):
 model = WarehouseCategory
 template_name = 'warehouse/category_delete_confirm.html'
 success_url = '/warehouse/categories'
 success_message = 'category deleted'
 error_message = 'failed category deleting'



# warehouse product
# warehouse product list
class WarehouseProductList(View):
 def get(self,request):
  products = Warehouse.objects.all()
  filters = WarehouseFilter(request.GET, queryset=products)
  products = filters.qs
  paginator = Paginator(products, 25)
  page_number = request.GET.get('paginator')
  products = paginator.get_page(page_number)
  context = {
   'products':products, 'filters':filters
  }
  return render(request, 'warehouse/warehouse.html', context)


# warehouse product create
class WarehouseProductCreate(SuccessMessageMixin,CreateView):
 form_class = WarehouseProductForm
 template_name = 'warehouse/warehouse_create.html'
 success_url = '/warehouse'
 success_message = 'product created'
 error_message = 'product creating failed'
 
# warehouse product update
class WarehouseProductUpdate(SuccessMessageMixin,UpdateView):
 model = Warehouse
 form_class = WarehouseProductForm
 template_name = 'warehouse/warehouse_create.html'
 success_url = '/warehouse'
 success_message = 'product updated'
 error_message = 'product updating failed'


# warehouse delete product
class WarehouseProductDelete(SuccessMessageMixin,DeleteView):
 model = Warehouse
 template_name = 'warehouse/warehouse_delete_confirm.html'
 success_url = '/warehouse'
 success_message = 'product deleted'
 error_message = 'product deleting failed'
