from django.db import models
from django.core.validators import RegexValidator
from . import Global
from django.db import models

# When abstract = True is set in the Meta class, it indicates that this model is an abstract base class. 
# An abstract base class is a class that is not meant to be instantiated on its own and will not have a corresponding table created in the database.

#Parent Class
class ServiceProvider(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=2, choices=Global.USERS.CITIES_CHOICES, default=Global.USERS.CITIES_CHOICES[0])
    industry = models.CharField(max_length=100,choices=Global.SERVICES.SERVICE_CATEGORIES, default=Global.SERVICES.SERVICE_CATEGORIES[0])
    bio = models.TextField(max_length=300)
    website = models.URLField(
        max_length=200,
        validators= [Global.VALIDATORS.website_validator] ,  # Apply the custom validator if needed
        blank=True,  # Allows the field to be empty in forms
        null=True     # Allows the field to be null in the database
    )
    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Freelancer(ServiceProvider):
    gender = models.CharField(max_length=1, choices=Global.USERS.GENDER, default=Global.USERS.GENDER[0])

class Customer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=Global.USERS.GENDER, default=Global.USERS.GENDER[0])
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        max_length=8,
        unique=True,
        validators=[RegexValidator(regex=r'^\d{8}$', message='Phone number must be exactly 8 digits')]
    )
    region = models.CharField(max_length=2, choices=Global.USERS.CITIES_CHOICES)

    def __str__(self):
        return self.name
    
class Company(ServiceProvider):
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"