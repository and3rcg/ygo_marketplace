from api.viewsets import CardViewSet, UserViewSet
from rest_framework import routers

api_router = routers.DefaultRouter()

api_router.register('card', CardViewSet)
api_router.register('user', UserViewSet)
