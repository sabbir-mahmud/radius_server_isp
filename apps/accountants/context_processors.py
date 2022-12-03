# imports
from .models import CompanyProfile


# get company profile
def company_profile(request):
 profile = CompanyProfile.objects.get(id=1)
 return {'profile':profile}