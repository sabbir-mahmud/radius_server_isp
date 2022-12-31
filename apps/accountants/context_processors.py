# imports
from .models import CompanyProfile


# get company profile
def company_profile(request):
    def create_profile():
        CompanyProfile.objects.create(name='Kaliganj Network', city='Ullapara', state='Rajshahi', country='Bangladesh')
        return CompanyProfile.objects.get(id=1) 
    profile = CompanyProfile.objects.get(id=1) if CompanyProfile.objects.all().exists() else create_profile()
    return {'profile':profile}