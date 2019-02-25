from django.shortcuts import render

# Create your views here.

from rest_framework import status

from rest_framework import mixins
from rest_framework import generics

from .serializers import GoodsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Goods

# class GoodsListView(APIView):
#     def get(self, request, format=None):
#         goods = Goods.objects.all()[:10]
#         goods_serializer = GoodsSerializer(goods, many=True)
#         return Response(goods_serializer.data)
#
#     def post(self, request, format=None):
#         serializer = GoodsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class GoodsListView(mixins.ListModelMixin, generics.GenericAPIView):
#     queryset = Goods.objects.all()[:10]
#     serializer_class = GoodsSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

class GoodsListView(generics.ListAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer