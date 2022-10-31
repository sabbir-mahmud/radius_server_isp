# imports

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include('apps.clients.urls')),
    path('warehouse/', include('apps.warehouse.urls')),
    path('onus/', include('apps.onu.urls')),
    path('pops/', include('apps.pop.urls')),
    path('tasks/', include('apps.tasks.urls')),
    path('dashboard/', include('apps.accountants.urls')),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
