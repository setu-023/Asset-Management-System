from django.urls import path

from employee.views import *
urlpatterns = [

    path('', EmployeeListCreateAPIView.as_view()),
    path('<int:pk>', EmployeeRetrieveUpdateDestroyAPIViewAPIView.as_view()),

]