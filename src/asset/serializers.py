from curses import meta
import imp
from rest_framework import serializers

from asset.models import *

class CompanySerializer(serializers.ModelSerializer):

    class meta:
        model = Asset
        fiedls = '__all__'

class DelegateAssetSerializer(serializers.ModelSerializer):

    class meta:
        model = DelegateAsset
        fiedls = '__all__'