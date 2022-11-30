from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.db.models import Q
import json

from account.models import *
from account.serializers import *
from asset.models import *
from asset.serializers import *
from company.models import *
from company.serializers import CompanyAccessSerializer
from employee.views import check_access


class AssetListCreateAPIView(APIView):

    permission_classes = [permissions.IsAuthenticated,]

    def post(self, request):
        
        try:
            user = User.objects.get(email=request.user).id
            company = CompanyAccess.objects.get(user=user)
            company = CompanyAccessSerializer(company).data
            print((company['company']))
            #assigning company id 
            request.data['company'] = company['company']
            serializer = AssetSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({ 'message': 'asset created', 'data':serializer.data}, status.HTTP_201_CREATED,)
            else:
                return Response({'message': 'something went wrong', 'data': serializer.errors}, status.HTTP_405_METHOD_NOT_ALLOWED,)
        except:
            return Response({'message': 'something went wrong', 'data': serializer.errors}, status.HTTP_405_METHOD_NOT_ALLOWED,)


    def get(self, request):
        
        assets = Asset.objects.all()
        serializer = AssetSerializer(assets, many=True)
        if serializer.data:
            return Response({'message': 'showing data', 'data':serializer.data}, status.HTTP_200_OK,)
        else:
            return Response({'message': 'no data found', 'data': []}, status.HTTP_404_NOT_FOUND)


class AssetRetrieveUpdateDestroyAPIViewAPIView(APIView):

    def get(self, request, pk, *args, **kwargs):
        
        #checking access for requested user
        has_access = check_access(request)
        if has_access:
            try:
                asset = Asset.objects.get(id=pk)
                serializer = AssetSerializer(asset)
                return Response({'message': 'showing data', 'data':serializer.data, 'status':status.HTTP_200_OK})
            except:
                return Response({'message': 'no data found', 'data': [], 'status':status.HTTP_404_NOT_FOUND})
        else:
            return Response({'message': 'authorization error', 'data': []}, status.HTTP_405_METHOD_NOT_ALLOWED,)


    def put(self, request, pk, *args, **kwargs):

        try:
            asset = Asset.objects.get(id=pk)
        except:
            return Response(data={'message': 'no data found', 'data': [], 'status':status.HTTP_404_NOT_FOUND})
 
        serializer = AssetSerializer(asset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'data updated', 'data':serializer.data, 'status':status.HTTP_200_OK})
        else:
            return Response({'message': 'something went wrong', 'data': serializer.errors, 'status':status.HTTP_405_METHOD_NOT_ALLOWED})


    def delete(self, request, pk, *args, **kwargs):

        try:
            asset = Asset.objects.get(id=pk)
            asset.delete()
            return Response({'message': 'data deleted', 'data':[], 'status':status.HTTP_200_OK})
        except:
            return Response({'message': 'no data found', 'data': [], 'status':status.HTTP_404_NOT_FOUND})

def check_access(request):

    user = User.objects.get(email=request.user).id
    print(user)
    try:
        access = CompanyAccess.objects.get(user=user)
        return True
    except Exception as e:
        print(e)
        return False


class AssetLogAPIView(APIView):

    permission_classes = [permissions.IsAuthenticated,]

    def get(self, request, pk):
        
        asset = DelegateAsset.objects.filter(asset=pk)
        if asset:
            serializer = AssetSerializer(asset, many=True).data
            return Response({ 'message': 'asset created', 'data':serializer}, status.HTTP_201_CREATED,)
        else:
            return Response({'message': 'no data found', 'data': []}, status.HTTP_404_NOT_FOUND)
