from django.views import View
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import CardSerializer, RegisterSerializer, UserSerializer
from .models import User, CardModel


class CardViewSet(viewsets.ModelViewSet):
    queryset = CardModel.objects.all()
    serializer_class = CardSerializer

class RegisterViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    http_method_names = ['post']
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

