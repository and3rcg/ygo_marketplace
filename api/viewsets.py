from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
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
    permission_classes = [IsAuthenticated]
    queryset = CardModel.objects.all()
    serializer_class = CardSerializer

class CardOnSaleViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = CardOnSale.objects.all()
    serializer_class = CardOnSaleSerializer

    def get_queryset(self):
        queryset = CardOnSale.objects.all()
        card_name = self.request.query_params.get('card_name')
        username = self.request.query_params.get('username')
        if card_name:
            queryset = queryset.filter(card__name=card_name)
        if username:
            queryset = queryset.filter(seller__username=username)
        return queryset

    def create(self, request, *args, **kwargs):
        card_data = request.data

        new_card = CardOnSale.objects.create(
            seller=User.objects.get(id=card_data['seller']),
            card=CardModel.objects.get(id=card_data['card']),
            price=card_data['price'],
            set=card_data['set'],
            rarity=card_data['rarity'],
            amount=card_data['amount'],
            region=card_data['region'],
            condition=card_data['condition'],
            is_visible=card_data['is_visible']
        )

        serializer = CardOnSaleSerializer(data=card_data)

        if serializer.is_valid(raise_exception=True):
            new_card.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)
    