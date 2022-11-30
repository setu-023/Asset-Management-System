from dataclasses import field
from pyexpat import model
from rest_framework import serializers

from employee.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):

    class meta:
        model = Employee
        fields = '__all__'