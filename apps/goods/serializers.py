# Author:Sunday
from goods.models import Goods, GoodsCategory
from rest_framework import serializers



class CategorySerializer3(serializers.ModelSerializer):
    """
    商品三级类别序列化
    """
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    """
    商品二级类别序列化
    """
    sub_cat = CategorySerializer3(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """
    商品一级类别序列化
    """
    sub_cat = CategorySerializer2(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    name = serializers.CharField(required=True, max_length=100)
    click_num = serializers.IntegerField(default=0)
    goods_front_image = serializers.ImageField()
    # category = CategorySerializer()
    # images = GoodsImageSerializer(many=True)

    def create(self, validated_data):
        return Goods.objects.create(**validated_data)


    class Meta:
        model = Goods
        # fields = ('category', 'goods_sn', 'name', 'click_num', 'goods_front_image', 'market_price')
        fields = "__all__"
