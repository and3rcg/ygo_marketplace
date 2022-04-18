from django.contrib.auth import get_user_model
from django.db.models import F
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import CardModel, CardOnSale, UserAddress, Orders
from .serializers import *

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


class AddressViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = AddressSerializer
    queryset = UserAddress.objects.all()

    def create(self, request):
        address_data = request.data
        current_user = request.user
        serializer = AddressSerializer(data=address_data)
        if serializer.is_valid(raise_exception=True):
            address = UserAddress.objects.create(**address_data, user=current_user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        # only return the authenticated user's addresses.
        current_user = request.user
        queryset = UserAddress.objects.filter(user=current_user)
        serializer = AddressSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


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

    def create(self, request):
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

    # create custom action "buy"
    @action(detail=True, methods=['post'])
    def buy(self, request, pk=None):
        """
        what should happen once a card is bought:
            the website (admin account) takes a 10% cut of the transaction;
            the seller takes the rest;
            a fixed shipping fee (5 USD) will be charged;
            deduce the amount bought off of the product's stock (and verify it's availability);
                if the stock goes to zero: set is_visible to False, and if negative, send HTTP 400;
            deduce the order's total price off of the buyer's wallet
        """

        # get product data through attributes e.g. product.amount
        product = self.get_object()

        # get request data through the get method e.g. request.data.get('amount') data in strings
        order_data = request.data
        amount_bought = int(order_data.get('amount'))

        # insert funds verification
        buyer = request.user
        seller = product.seller
        admin = User.objects.get(username='admin')

        order_price = amount_bought * product.price
        order_total_price = order_price + 5  # fixed 5 USD shipping fee

        print(admin.wallet)

        if buyer.wallet > order_total_price:
            if (amount_bought > 0) and (amount_bought <= product.amount):
                admin.wallet = F('wallet') + 0.1*order_price
                admin.save()
                seller.wallet = F('wallet') + 0.9*order_price
                seller.save()
                buyer.wallet = F('wallet') - order_total_price
                buyer.save()
                # create order object
                # deduce product amount (if zero then set hidden)
                return Response(status=status.HTTP_201_CREATED)
            return Response({'error': 'Invalid amount.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'error': 'Insufficient funds.'}, status=status.HTTP_400_BAD_REQUEST)
        # return 400 insufficient funds

        # serializer = PasswordSerializer(data=request.data)


class OrderViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    queryset = Orders.objects.all()

    def list(self, request):
        return super().list(request)
