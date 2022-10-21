from email.policy import default
from tabnanny import verbose
from django.db import models
from django.forms import ImageField

# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=200)
    weitht = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    desscription = models.TextField(blank=True)
    composition = models.TextField(blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to="img/")

    
class Dish(Product):
    category = models.ForeignKey('Category_food', on_delete=models.PROTECT, null=True)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "dish"
        verbose_name_plural = "dishes"


class Drink(Product):
    category = models.ForeignKey('Category_drink', on_delete=models.PROTECT, null=True)
    kind = models.ForeignKey('Kind_drink', on_delete=models.PROTECT, null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "drink"
        verbose_name_plural = "drinks"



class Category_food(models.Model):
    category = models.CharField(max_length=50, db_index=True)
    
    def __str__(self):
        return self.category
    class Meta:
        verbose_name = "food category"
        verbose_name_plural = "food categories"

class Category_drink(models.Model):
    category = models.CharField(max_length=50, db_index=True)
    
    def __str__(self):
        return self.category
    class Meta:
        verbose_name = "drink category"
        verbose_name_plural = "drink categories"

class Kind_drink(models.Model):
    kind = models.CharField(max_length=50, db_index=True)
    def __str__(self):
        return self.kind
    class Meta:
        verbose_name = "drink kind"
        verbose_name_plural = "drink kinds"
    