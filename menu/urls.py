from django.urls import path

from rest_framework import routers
# from .api import DishViewSet

from . import views

router = routers.DefaultRouter()
# router.register('/index', views.index, 'index')


# router.register('api/dish', DishViewSet, 'dish')

urlpatterns = router.urls

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('dishes', views.show_dishes, name='show_dishes'),
# ]

urlpatterns = [
    path('api/menu', views.MenuApiView.as_view())
]