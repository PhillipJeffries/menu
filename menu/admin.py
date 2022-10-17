from django.contrib import admin

from .models import Dish, Category

class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


# Register your models here.
admin.site.register(Dish, MenuAdmin)
admin.site.register(Category)


