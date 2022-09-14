from django.contrib import admin

from .models import Employ, EmployCategory

# Register your models here.
admin.site.register(EmployCategory)
admin.site.register(Employ)
