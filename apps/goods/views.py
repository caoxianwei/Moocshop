from django.shortcuts import render

# Create your views here.

from rest_framework import status

from rest_framework import mixins
from rest_framework import generics

from .serializers import GoodsSerializer
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from goods.filters import GoodsFilter
from .models import Goods

# 商品列表分页类
class GoodsPagination(PageNumberPagination):
    page_size = 12
    # 向后台要多少条
    page_size_query_param = 'page_size'
    # 定制多少页的参数
    page_query_param = "page"
    max_page_size = 100

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

class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表页，分页，搜索，过滤，排序,取某一个具体商品的详情
    """
    pagination_class = GoodsPagination
    serializer_class = GoodsSerializer
    queryset = Goods.objects.all()

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ('name', 'shop_price')

    filter_class = GoodsFilter

    search_fields = ('name', 'goods_brief', 'goods_desc')

    ordering_fields = ('sold_num', 'shop_price')

    # def get_queryset(self):
    #     price_min =self.request.query_params.get('price_min', 0)
    #     if price_min:
    #         Goods.objects.filter(shop_price__gt=int(price_min))
    #     return Goods.objects.filter(shop_price__gt=100)