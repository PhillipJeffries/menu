# from dataclasses import field, fields
from rest_framework import serializers
from .models import *

class DishSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = Dish
        fields = '__all__'

class DrinkSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    kind = serializers.StringRelatedField()
    class Meta:
        model = Drink
        fields = '__all__'


