# imports
from django.contrib import admin

from .models import Commission, CompanyProfile, Earning, Invest, Owner

# Register your models here.
admin.site.register(CompanyProfile)
admin.site.register(Owner)
admin.site.register(Invest)
admin.site.register(Earning)
admin.site.register(Commission)
