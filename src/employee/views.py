from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.db.models import Q

from account.models import *
from account.serializers import *
from employee.models import *
from employee.serializers import *
from company.models import *


class EmployeeListCreateAPIView(APIView):

    permission_classes = [permissions.IsAuthenticated,]

    def post(self, request):
        
        try:
            employee = Employee.objects.get(user=request.data['user'], company=request.data['company'])
            return Response({'message': 'duplicate data', 'data': []}, status.HTTP_405_METHOD_NOT_ALLOWED,)
        except:
            has_access = check_access(request)
            if has_access:
                serializer = EmployeeSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({ 'message': 'employee created', 'data':serializer.data}, status.HTTP_201_CREATED,)
                else:
                    return Response({'message': 'something went wrong', 'data': serializer.errors}, status.HTTP_200_OK,)
            else:
                return Response({'message': 'authorization error', 'data': []}, status.HTTP_405_METHOD_NOT_ALLOWED,)

    def get(self, request):
        
        companies = Employee.objects.all()
        serializer = EmployeeSerializer(companies, many=True)
        if serializer.data:
            return Response({'message': 'showing data', 'data':serializer.data}, status.HTTP_200_OK,)
        else:
            return Response({'message': 'no data found', 'data': []}, status.HTTP_404_NOT_FOUND)


class EmployeeRetrieveUpdateDestroyAPIViewAPIView(APIView):

    def get(self, request, pk, *args, **kwargs):
        print(pk)
        try:
            employee = Employee.objects.get(id=pk)
            serializer = EmployeeSerializer(employee)
            return Response({'message': 'showing data', 'data':serializer.data, 'status':status.HTTP_200_OK})
        except:
            return Response({'message': 'no data found', 'data': [], 'status':status.HTTP_404_NOT_FOUND})


    def put(self, request, pk, *args, **kwargs):

        print(pk)
        print(request.data)
        try:
            employee = Employee.objects.get(id=pk)
        except:
            return Response(data={'message': 'no data found', 'data': [], 'status':status.HTTP_404_NOT_FOUND})
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'data updated', 'data':serializer.data, 'status':status.HTTP_200_OK})
        else:
            return Response({'message': 'something went wrong', 'data': serializer.errors, 'status':status.HTTP_405_METHOD_NOT_ALLOWED})


    def delete(self, request, pk, *args, **kwargs):

        try:
            print(pk)
            employee = Employee.objects.get(id=pk)
            employee.delete()
            return Response({'message': 'data deleted', 'data':[], 'status':status.HTTP_200_OK})
        except:
            return Response({'message': 'no data found', 'data': [], 'status':status.HTTP_404_NOT_FOUND})


def check_access(request):

    user = User.objects.get(email=request.user).id
    print(user)
    try:
        access = CompanyAccess.objects.get(user=user, company=request.data['company'])
        return True
    except Exception as e:
        print(e)
        return False