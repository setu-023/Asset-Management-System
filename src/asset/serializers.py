from curses import meta
import imp
from rest_framework import serializers

from asset.models import *

class AssetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asset
        fields = '__all__'

class DelegateAssetSerializer(serializers.ModelSerializer):

    class Meta:
        model = DelegateAsset
        fields = '__all__'