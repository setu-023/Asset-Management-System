import imp
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from account.views import *

urlpatterns = [

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', AccountListCreateAPIView.as_view(), name='register'),

]