from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        User = get_user_model()
        model = User
        exclude = ('password',)