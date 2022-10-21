from rest_framework.response import Response

from rest_framework import generics

from rest_framework.views import APIView

from .models import Dish, Drink

from .serializers import *




# class MenuApiView(APIView):
#     def get(self, request):
#         dishes = Dish.objects.all().values()
#         drinks = Drink.objects.all().values()
#         return Response({'menu': {'dishes': dishes, 'drinks': drinks}})
    



class MenuApiView(APIView):
    def get(self, request):
        dishes = Dish.objects.all()
        drinks = Drink.objects.all()
        return Response({'dishes': DishSerializer(dishes, many=True).data,
                        'drnks': DrinkSerializer(drinks, many=True).data})