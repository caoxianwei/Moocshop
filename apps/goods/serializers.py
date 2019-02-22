# Author:Sunday
from goods.models import Goods
from rest_framework import serializers


class GoodsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, max_length=100)
    click_num = serializers.IntegerField(default=0)
    # category = CategorySerializer()
    # images = GoodsImageSerializer(many=True)

    class Meta:
        model = Goods
        # fields = ('category', 'goods_sn', 'name', 'click_num', 'sold_num', 'market_price')
        fields = "__all__"
