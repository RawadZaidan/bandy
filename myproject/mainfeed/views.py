# mainfeed/views.py
from django.shortcuts import render
from .models import Freelancer, Company
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q

def freelancers_page(request):
    query = request.GET.get('q')
    if query:
        freelancers = Freelancer.objects.filter(
            Q(name__icontains=query) | 
            Q(location__icontains=query) | 
            Q(industry__icontains=query)
        )
    else:
        freelancers = Freelancer.objects.all()
    return render(request, 'mainfeed/freelancers_page.html', {'freelancers': freelancers})

def home(request):
    return render(request, 'mainfeed/home.html')

def companies_page(request):
    query = request.GET.get('q')
    if query:
        companies = Company.objects.filter(
            Q(name__icontains=query) | 
            Q(location__icontains=query) | 
            Q(industry__icontains=query)
        )
    else:
        companies = Company.objects.all()
    return render(request, 'mainfeed/companies_page.html', {'companies': companies})