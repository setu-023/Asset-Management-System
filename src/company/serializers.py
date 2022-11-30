from rest_framework import serializers

from company.models import *

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'

class CompanyAccessSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyAccess
        fields = '__all__'