from rest_framework.response import Response

from rest_framework.views import APIView

from .models import Dish, Drink




class MenuApiView(APIView):
    def get(self, request):
        dishes = Dish.objects.all().values()
        drinks = Drink.objects.all().values()
        return Response({'menu': {'dishes': dishes, 'drinks': drinks}})
    
