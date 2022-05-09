from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models


class User(AbstractUser):
    '''
    Customize the Django authentication system
    This model will use the default values from Django's authentication system, and will add some
    profile-specific fields, such as address and sales amount
    '''
    bio = models.TextField(blank=True)
    sales = models.IntegerField(null=False, blank=False, default=0, verbose_name='Sales Amount')
    wallet = models.FloatField(null=False, blank=False, default=0, verbose_name='Wallet funds')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self) -> str:
        return str(self.username)


class UserAddress(models.Model):
    country = models.CharField(max_length=100, verbose_name='Country')
    state_province = models.CharField(max_length=100, verbose_name='State/Province')
    city = models.CharField(max_length=100, verbose_name='City')
    street = models.CharField(max_length=100, verbose_name='Street')
    zip_code = models.CharField(max_length=10, verbose_name='Zip Code')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}: {self.street} {self.zip_code}'


class CardModel(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False,
                            blank=False, default='name', verbose_name='Name')
    attribute = models.CharField(max_length=20, null=True, blank=True, verbose_name='Attribute')
    race = models.CharField(max_length=20, null=False, blank=False,
                            default='race', verbose_name='Class')
    level = models.IntegerField(null=True, blank=True, verbose_name='Level/Rank/Link')
    attack = models.IntegerField(null=True, blank=True, verbose_name='ATK')
    defense = models.IntegerField(null=True, blank=True, verbose_name='DEF')
    description = models.TextField(null=False, blank=False,
                                   default='desc', verbose_name='Effect/Description')
    type = models.CharField(max_length=100, null=False, blank=False,
                            default='type', verbose_name='Type')
    image_url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.name)


class CardOnSale(models.Model):
    localization_choices = [
        ('PT_BR', 'Brazilian Portuguese'),
        ('EN_US', 'English'),
        ('FR', 'French'),
        ('IT', 'Italian'),
        ('DE', 'German'),
        ('ES', 'Spanish'),
        ('JP', 'Japanese'),
        ('KR', 'Korean'),
        ('CN', 'Chinese'),
        ('EN_OCG', 'English (Asian)'),
    ]
    condition_choices = [
        ('NM', 'Near Mint'),
        ('LP', 'Lightly Played'),
        ('MP', 'Moderately Played'),
        ('HP', 'Heavily Played'),
        ('DMG', 'Damaged'),
    ]

    seller = models.ForeignKey(User, on_delete=models.CASCADE, default=0, verbose_name='Seller')
    card = models.ForeignKey(CardModel, on_delete=models.CASCADE, verbose_name='Card name')
    price = models.FloatField(null=False, blank=False, default=1, validators=[MinValueValidator(1)])
    set = models.CharField(max_length=20, null=False, blank=False, default='XXXX-000', verbose_name='Set')
    rarity = models.CharField(max_length=40, null=False, blank=False, default='rare')
    amount = models.IntegerField(null=False, blank=False, default=1, validators=[MinValueValidator(1)], verbose_name='Amount')
    region = models.CharField(max_length=20, choices=localization_choices, verbose_name='Region')
    condition = models.CharField(max_length=20, choices=condition_choices, verbose_name='Condition')
    is_visible = models.BooleanField(blank=False, null=False, default=True, verbose_name='Visible?')
    created_at = models.DateTimeField(default=datetime.now, verbose_name='Creation date')

    def __str__(self) -> str:
        # this returns __str__(self) from CardModel, so, it'll return the card's name (line 41)
        return f'{str(self.card)} sold by {str(self.seller)}'


class Orders(models.Model):
    customer = models.ForeignKey(User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        verbose_name='Customer',
        related_name='customer',
        )
    seller = models.ForeignKey(User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        verbose_name='Seller',
        related_name='seller',
        )
    complete = models.BooleanField(default=False) # if complete == False: cart can be updated
    customer_address = models.ForeignKey(UserAddress, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(default=datetime.now, verbose_name='Creation date')
    updated_at = models.DateTimeField(default=datetime.now, verbose_name='Latest update')
    transaction_id = models.CharField(max_length=100, unique=True, blank=True, null=True)
    shipping_fee = models.IntegerField(default=5, blank=True, null=True, verbose_name='Shipping fee')
    
    def __str__(self) -> str:
        return self.transaction_id


class OrderItem(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(CardOnSale, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField(null=False, blank=False, default=0)
    price = models.FloatField(null=False, blank=False, default=0)
    date_added = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return f'{self.product.__str__()} ({self.order.__str__()})'

