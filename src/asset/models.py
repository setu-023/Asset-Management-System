from argparse import ONE_OR_MORE
from django.db import models
import uuid

from company.models import Company
from employee.models import Employee

class Asset(models.Model):

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    DEVICE_TYPE = (
        ("mobile","mobile"),
        ("tablet","tablet"),
        ("laptop","laptop"),
    )
    device_type = models.CharField(max_length=25, choices=DEVICE_TYPE)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class DelegateAsset(models.Model):

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    DETEGATE_TYPE = (
       ( "allocated","allocated"),
       ("returned", "returned"),
    )
    type = models.CharField(max_length=25, choices=DETEGATE_TYPE)
    DEVICE_CONDITION_TYPE = (
       ( "good","good"),
       ("average", "average"),
       ("bad", "bad")
    )
    device_condition = models.CharField(max_length=25, choices=DEVICE_CONDITION_TYPE)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)