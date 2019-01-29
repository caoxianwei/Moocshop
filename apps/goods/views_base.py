# Author:Sunday

from goods.models import Goods


from django.views.generic.base import View



class GoodsListView(View):
    def get(self, request):
        """
        通过django的view实现商品列表页
        """
        json_list = []
        goods = Goods.objects.all()[:10]

        for good in goods:
            json_dict = {}
            json_dict["name"] = good.name
            json_dict["category"] = good.category.name
            json_dict["market_price"] = good.market_price
            # json_dict["add_time"] = good.add_time
            json_list.append(json_dict)

        from django.http import HttpResponse
        import json
        return HttpResponse(json.dumps(json_list),content_type="application/json")


