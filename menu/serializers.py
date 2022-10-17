from dataclasses import field, fields
from rest_framework import serializers
from .models import Category, Dish

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category', )



class DishSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    class Meta:
        model = Dish
        fields = ('id', 'name', 'price', 'category', )
        # fields = "__all__"