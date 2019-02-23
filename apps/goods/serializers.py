# Author:Sunday
from goods.models import Goods, GoodsCategory
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
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
