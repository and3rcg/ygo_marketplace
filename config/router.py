from api.viewsets import *
from rest_framework import routers

api_router = routers.DefaultRouter()

api_router.register('card', CardViewSet)
api_router.register('on_sale', CardOnSaleViewSet)
api_router.register('address', AddressViewSet)
api_router.register('orders', OrderViewset)
