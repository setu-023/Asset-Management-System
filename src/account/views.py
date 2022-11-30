from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework import permissions, status
from rest_framework.response import Response

from account.serializers import UserSerializer


class AccountListCreateAPIView(ListCreateAPIView):

    def get_permissions(self):
    
        if self.request.method == 'POST':
            return (permissions.AllowAny(),)
        

    def create(self, request, *args, **kwargs):

        try:
            User = get_user_model()
            user = User.objects.create_user(
                email=self.request.data['email'],
            )  
            #hashing the password         
            user.set_password(self.request.data['password'])
            user.save()
            user = UserSerializer(user).data

            return Response({'message':'user created', 'data':user, 'status':status.HTTP_201_CREATED})
        except Exception as e:
            print(e)
            return Response({'message': f'cannot create user. reason: {e}', 'data':[], 'status':status.HTTP_409_CONFLICT})


