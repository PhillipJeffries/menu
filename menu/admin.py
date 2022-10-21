from django.contrib import admin

from .models import *
# Dish, Drink, Category_food, Category_drink

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


# Register your models here.
admin.site.register(Category_food)
admin.site.register(Category_drink)
admin.site.register(Kind_drink)
admin.site.register(Dish, MenuAdmin)
admin.site.register(Drink)


