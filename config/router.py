from api.viewsets import CardViewSet, RegisterViewSet, UserViewSet
from rest_framework import routers

api_router = routers.DefaultRouter()

api_router.register('card', CardViewSet)
api_router.register('register', RegisterViewSet)

# TODO remove this when done tinkering with axios
api_router.register('user', UserViewSet)
