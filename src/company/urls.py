from django.urls import path

from company.views import *
urlpatterns = [

    path('', CompanyListCreateAPIView.as_view()),
    path('<int:pk>', CompanyRetrieveUpdateDestroyAPIViewAPIView.as_view()),

]