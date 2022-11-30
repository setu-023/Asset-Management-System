from rest_framework import serializers

from company.models import *

class CompanySerializer(serializers.ModelSerializer):

    class meta:
        model = Company
        fiedls = '__all__'

class CompanyAccessSerializer(serializers.ModelSerializer):

    class meta:
        model = CompanyAccess
        fiedls = '__all__'