from django.urls import path

from asset.views import *
urlpatterns = [

    path('', AssetListCreateAPIView.as_view()),
    path('<int:pk>', AssetRetrieveUpdateDestroyAPIViewAPIView.as_view()),

]