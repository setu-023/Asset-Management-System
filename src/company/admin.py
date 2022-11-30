from django.contrib import admin

from company.models import *

admin.site.register(Company)
admin.site.register(CompanyAccess)