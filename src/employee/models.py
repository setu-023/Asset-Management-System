from operator import mod
from django.db import models

from account.models import *
from company.models import *


class Employee(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company =  models.ForeignKey(Company, on_delete=models.CASCADE)
    
    # department = models.CharField(max_length=255, choices=DEPARTMENT_TYPE)
    #designation = models.CharField(max_length=255, choices=DESIGNATION_TYPE)

    ROLE_TYPE = (
       ( "admin","admin"),
       ("executive", "executive"),
       ("manager", "manager")
    )
    role = models.CharField(max_length=25, choices=ROLE_TYPE)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)