from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import CardSerializer, CardOnSaleSerializer
from .models import CardModel, CardOnSale

User = get_user_model()

class BlacklistTokenViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]
    http_method_names = ['post']
    def create(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class CardViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = CardModel.objects.all()
    serializer_class = CardSerializer

class CardOnSaleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = CardOnSale.objects.filter(is_visible=True).distinct('card')
    serializer_class = CardOnSaleSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.query_params:
            card_name = self.request.query_params.get('card_name')
            username = self.request.query_params.get('username')
            card_id = self.request.query_params.get('card_id')
            if card_name:
                queryset = CardOnSale.objects.filter(card__name=card_name, is_visible=True)
            if username:
                queryset = CardOnSale.objects.filter(seller__username=username, is_visible=True)
            if card_id:
                queryset = CardOnSale.objects.filter(card__id=card_id, is_visible=True)
        return queryset

    def create(self, request, *args, **kwargs):
        card_data = request.data
        current_user = request.user

        serializer = CardOnSaleSerializer(data=card_data)
        serializer.is_valid(raise_exception=True)

        # control for duplicate cards by seller and card
        _, created = CardOnSale.objects.get_or_create(
            seller=current_user, 
            card=card_data['card'], 
            defaults=serializer.validated_data
            )
        
        if created:
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_409_CONFLICT)
    