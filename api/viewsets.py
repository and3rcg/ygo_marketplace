from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .mappings import filters_mapping
from .models import CardModel, CardOnSale, OrderItem, UserAddress, Orders
from .serializers import *
from .scripts.payment import make_transaction
from .scripts.transaction import generate_transaction_id

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
            UserAddress.objects.create(
                user=current_user,
                **serializer.validated_data
            )
            return Response(data=serializer.validated_data, status=status.HTTP_201_CREATED)

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
        # make a mapping of query params: https://github.com/manjitkumar/drf-url-filters

        if self.request.query_params:
            query_params = self.request.query_params
            url_params = {'is_visible': True} # default

            for item in query_params:
                if item in filters_mapping:
                    query_kwarg = filters_mapping.get(item)
                    url_params[query_kwarg] = query_params.get(item)
            queryset = CardOnSale.objects.filter(**url_params)

            # card_name = query_params.get('card_name')
            # username = query_params.get('username')
            # card_id = query_params.get('card_id')

            # if card_name: # use "__icontains" for search?
            #     queryset = CardOnSale.objects.filter(card__name__icontains=card_name, is_visible=True)

            # if username: # get all cards sold by a specific user
            #     queryset = CardOnSale.objects.filter(seller__username=username, is_visible=True)

            # if card_id: # get all users selling a specific card
            #     queryset = CardOnSale.objects.filter(card__id=card_id, is_visible=True)

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

    # create custom action "add to cart: get_or_create Order object"
    @action(detail=True, methods=['post'])
    def add_to_cart(self, request, pk=None):
        """
        what should happen once a card is bought:
            the website (admin account) takes a 10% cut of the make_transaction;
            the seller takes the rest;
            a fixed shipping fee (5 USD) will be charged;
            deduce the amount bought off of the product's stock (and verify it's availability);
                if the stock goes to zero: set is_visible to False, and if negative, send HTTP 400;
            deduce the order's total price off of the customer's wallet
        """
        # get product data through attributes e.g. product.amount
        product = self.get_object()

        # get request data through the get method e.g. request.data.get('amount') data in strings
        order_data = request.data
        buy_amount = int(order_data.get('amount'))

        customer = request.user
        seller = product.seller

        order_price = buy_amount * product.price

        # create an order for each seller
        order, created = Orders.objects.get_or_create(
            customer = customer,
            seller = seller,
            complete = False,
            defaults = {'transaction_id': generate_transaction_id(10)}
        )

        cart_item = OrderItem.objects.create(
            order = order,
            product = product,
            amount = buy_amount,
            price = order_price,
        )
        
        serialized_order = OrderSerializer(order)

        if created:
            return Response(data=serialized_order.data, status=status.HTTP_201_CREATED)

        return Response(data=serialized_order.data, status=status.HTTP_200_OK)


class OrderViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    queryset = Orders.objects.all()

    def get_queryset(self):
        queryset = Orders.objects.filter(customer=self.request.user)
        return queryset

    @action(methods=['post'], detail=True)
    # TODO create a checkout endpoint action to add address and set complete to True
    def checkout(self, request, pk=None):
        """
        what should happen here: 
            filter cards bought by seller
            set address in the Order object
            apply shipping fee
            apply validations and make the transaction
        """
        current_order = self.get_object()
        # get customer data
        customer = current_order.customer
        address_id = int(request.data.get('address_id'))
        address = UserAddress.objects.get(pk=address_id)
        
        seller = current_order.seller # get seller object

        if current_order.complete is True:
            return Response(data={'error': 'Order is already complete!'}, status = status.HTTP_400_BAD_REQUEST)
        
        order_items = OrderItem.objects.filter(order=current_order)
        order_price = 0

        # checkout validations
        for item in order_items:
            if item.amount > item.product.amount:
                return Response(data={'error': 'Invalid amount.'}, status = status.HTTP_400_BAD_REQUEST)
            order_price += item.amount * item.price
        
        if address.user != customer:
            return Response(data={'error': 'Invalid address data.'}, status = status.HTTP_400_BAD_REQUEST)
        
        if order_price + current_order.shipping_fee > customer.wallet:
            return Response(data={'error': 'Insufficient funds.'}, status = status.HTTP_400_BAD_REQUEST)

        # transaction process
        for item in order_items:
            # deduce the amount of cards bought from the listings
            item.product.amount = item.product.amount - item.amount
            if item.product.amount == 0:
                item.product.is_visible = False
            item.product.save()

        
        # transaction: admin (the website) takes a 10% cut
        admin = User.objects.get(username='admin')
        shipping_fee = current_order.shipping_fee

        make_transaction(customer, order_price+shipping_fee, deduce=True)
        make_transaction(seller, 0.9*order_price, deduce=False)
        make_transaction(admin, 0.1*order_price, deduce=False)

        # updating the order
        current_order.customer_address = address
        current_order.complete = True
        current_order.save()

        serializer = OrderSerializer(current_order)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
