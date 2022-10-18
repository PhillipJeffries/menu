from tabnanny import verbose
from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField("category", max_length=50)
    
    def __str__(self):
        return self.category
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"




class Dish(models.Model):
    name = models.CharField("dish", max_length=200)
    price = models.IntegerField(default=0)
    category = models.ManyToManyField(Category)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "dish"
        verbose_name_plural = "dishes"
