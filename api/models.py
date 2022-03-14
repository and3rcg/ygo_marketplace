from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator


class User(AbstractUser):
    """
    Customize the Django authentication system
    """
    USERNAME_FIELD = 'username'


class UserAddress(models.Model):
    country = models.CharField(max_length=100, verbose_name='Country')
    state_province = models.CharField(max_length=100, verbose_name='State/Province')
    city = models.CharField(max_length=100, verbose_name='City')
    street = models.CharField(max_length=100, verbose_name='Street')
    zip_code = models.CharField(max_length=10, verbose_name='Zip Code')

class UserProfile(models.Model):
    """
    This model will use the default values from Django's authentication system, and will add some
    profile-specific fields, such as address and sales amount
    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    sales = models.IntegerField(null=False, blank=False, default=0, verbose_name='Sales Amount')
    address = models.ForeignKey(UserAddress, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.user)


class CardModel(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, default='name', verbose_name='Name')
    attribute = models.CharField(max_length=20, null=True, blank=True, verbose_name='Attribute')
    race = models.CharField(max_length=20, null=False, blank=False, default='race', verbose_name='Class')
    level = models.IntegerField(null=True, blank=True, verbose_name='Level/Rank/Link')
    attack = models.IntegerField(null=True, blank=True, verbose_name='ATK')
    defense = models.IntegerField(null=True, blank=True, verbose_name='DEF')
    description = models.TextField(null=False, blank=False, default='desc', verbose_name='Effect/Description')
    type = models.CharField(max_length=100, null=False, blank=False, default='type', verbose_name='Type')



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


    seller = models.ForeignKey(User, on_delete = models.CASCADE, default=0, verbose_name='Seller ID')
    card = models.ForeignKey(CardModel, on_delete=models.CASCADE, verbose_name='Card ID')
    price = models.FloatField(null=False, blank=False, default=1, validators=[MinValueValidator(1)], verbose_name='Price')
    set = models.CharField(max_length=20,null=False, blank=False, default='XXXX-000', verbose_name='Set')
    rarity = models.CharField(max_length=40,null=False, blank=False, default='rare', verbose_name='Rarity')
    amount = models.IntegerField(null=False, blank=False, default=1, validators=[MinValueValidator(1)], verbose_name='Amount')
    region = models.CharField(max_length=20, choices=localization_choices, verbose_name='Region')
    condition = models.CharField(max_length=20, choices=condition_choices, verbose_name='Condition')


