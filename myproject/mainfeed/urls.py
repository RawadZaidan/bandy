# mainfeed/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("freelancers/", views.freelancers_page, name='freelancers'),
    path("companies/", views.companies_page, name='companies'),
]