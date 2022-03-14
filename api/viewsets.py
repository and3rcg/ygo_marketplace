from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from . import models, serializers
from .models import User


class CardViewSet(viewsets.ModelViewSet):
    queryset = models.CardModel.objects.all()
    serializer_class = serializers.CardSerializer


class UserViewSet(viewsets.ModelViewSet): 
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated]


