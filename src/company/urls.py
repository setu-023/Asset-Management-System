from django.urls import path

from company.views import *
urlpatterns = [

    path('', CompanyListCreateAPIView.as_view(), name='token_obtain_pair'),
    path('<int:pk>', CompanyRetrieveUpdateDestroyAPIViewAPIView.as_view(), name='register'),

]