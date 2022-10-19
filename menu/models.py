from tabnanny import verbose
from django.db import models

# Create your models here.

class Category_food(models.Model):
    category = models.CharField(max_length=50)
    
    def __str__(self):
        return self.category
    class Meta:
        verbose_name = "food category"
        verbose_name_plural = "food categories"

class Category_drink(models.Model):
    category = models.CharField(max_length=50)
    
    def __str__(self):
        return self.category
    class Meta:
        verbose_name = "drink category"
        verbose_name_plural = "drink categories"


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    desscription = models.TextField(blank=True)
    composition = models.TextField(blank=True)

    
class Dish(Product):
    category = models.ForeignKey('Category_food', on_delete=models.PROTECT, null=True)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "dish"
        verbose_name_plural = "dishes"


class Drink(Product):
    category = models.ForeignKey('Category_drink', on_delete=models.PROTECT, null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "drink"
        verbose_name_plural = "drinks"
    