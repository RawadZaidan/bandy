from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Freelancer, Customer, Company

admin.site.register(Freelancer)
admin.site.register(Customer)
admin.site.register(Company)