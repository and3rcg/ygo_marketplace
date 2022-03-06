from rest_framework import viewsets
from . import models, serializers


class CardViewSet(viewsets.ModelViewSet):
    queryset = models.CardModel.objects.all()
    serializer_class = serializers.CardSerializer
