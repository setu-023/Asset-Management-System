from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.db.models import Q

from account.models import *
from account.serializers import *
from company.models import *
from company.serializers import *

class CompanyListCreateAPIView(APIView):

    permission_classes = [permissions.IsAuthenticated,]

    def post(self, request):
        
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            company_access_data = {}
            print(serializer.data['id'])
            #creating access for requested user
            company_access_data['user'] = User.objects.get(email=request.user).id
            company_access_data['company'] = serializer.data['id']
            print(company_access_data)
            access_serializer = CompanyAccessSerializer(data=company_access_data)
            if access_serializer.is_valid():
                access_serializer.save()
            else:
                return Response({'message': 'something went wrong', 'data': access_serializer.errors}, status.HTTP_200_OK,)

            return Response({ 'message': 'company created', 'data':serializer.data}, status.HTTP_201_CREATED,)
        else:
            return Response({'message': 'something went wrong', 'data': serializer.errors}, status.HTTP_200_OK,)


    def get(self, request):
        
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        if serializer.data:
            return Response({'message': 'showing data', 'data':serializer.data}, status.HTTP_200_OK,)
        else:
            return Response({'message': 'no data found', 'data': []}, status.HTTP_404_NOT_FOUND)


class CompanyRetrieveUpdateDestroyAPIViewAPIView(APIView):

    def get(self, request, pk, *args, **kwargs):
        print(pk)
        try:
            company = Company.objects.get(id=pk)
            serializer = CompanySerializer(company)
            return Response({'message': 'showing data', 'data':serializer.data, 'status':status.HTTP_200_OK})
        except:
            return Response({'message': 'no data found', 'data': [], 'status':status.HTTP_404_NOT_FOUND})


    def put(self, request, pk, *args, **kwargs):

        print(pk)
        print(request.data)
        try:
            company = Company.objects.get(id=pk)
        except:
            return Response(data={'message': 'no data found', 'data': [], 'status':status.HTTP_404_NOT_FOUND})
        serializer = CompanySerializer(company, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'data updated', 'data':serializer.data, 'status':status.HTTP_200_OK})
        else:
            return Response({'message': 'something went wrong', 'data': serializer.errors, 'status':status.HTTP_405_METHOD_NOT_ALLOWED})


    def delete(self, request, pk, *args, **kwargs):

        try:
            print(pk)
            company = Company.objects.get(id=pk)
            company.delete()
            return Response({'message': 'data deleted', 'data':[], 'status':status.HTTP_200_OK})
        except:
            return Response({'message': 'no data found', 'data': [], 'status':status.HTTP_404_NOT_FOUND})



