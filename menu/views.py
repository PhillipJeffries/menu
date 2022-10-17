from django.shortcuts import render

from django.http import HttpResponse

from .models import Dish


def index(request):
    return HttpResponse("Why so long?")

def show_dishes(request):
    dishes = Dish.objects.all()
    return HttpResponse(dishes)



# Create your views here.
