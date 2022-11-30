from enum import unique
from turtle import update
from unicodedata import name
from django.db import models
from django.forms import CharField

from account.models import User

class Company(models.Model):

    name = CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=15)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class CompanyAccess(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    ROLE_TYPE = (
       ( "admin","admin"),
       ("executive", "executive")
    )
    role = models.CharField(max_length=25, choices=ROLE_TYPE, default='admin')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
