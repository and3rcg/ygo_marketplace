from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class CardModel(models.Model):
    card_name = models.CharField(max_length=100, null=False, blank=False, default='name', verbose_name='Name')
    card_attribute = models.CharField(max_length=20, null=True, blank=True, verbose_name='Attribute')
    card_race = models.CharField(max_length=20, null=False, blank=False, default='race', verbose_name='Class')
    card_level = models.IntegerField(null=True, blank=True, verbose_name='Level/Rank/Link')
    card_atk = models.IntegerField(null=True, blank=True, verbose_name='ATK')
    card_def = models.IntegerField(null=True, blank=True, verbose_name='DEF')
    card_description = models.TextField(null=False, blank=False, default='desc', verbose_name='Effect/Description')
    card_type = models.CharField(max_length=100, null=False, blank=False, default='type', verbose_name='Type')

# create class for card to sell, that includes the set's code and rarity
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


    seller_id = models.ForeignKey(User, on_delete = models.CASCADE, default=0, verbose_name='Seller ID')
    card_id = models.ForeignKey(CardModel, on_delete=models.CASCADE, verbose_name='Card ID')
    price = models.FloatField(null=False, blank=False, default=1, validators=[MinValueValidator(1)], verbose_name='Price')
    card_set = models.CharField(max_length=20,null=False, blank=False, default='XXXX-000', verbose_name='Set')
    card_rarity = models.CharField(max_length=40,null=False, blank=False, default='rare', verbose_name='Rarity')
    card_amount = models.IntegerField(null=False, blank=False, default=1, validators=[MinValueValidator(1)], verbose_name='Amount')
    card_region = models.CharField(max_length=20, choices=localization_choices, verbose_name='Region')
    card_condition = models.CharField(max_length=20, choices=condition_choices, verbose_name='Condition')

    # card_id: foreign key (CardModel) (card name maybe?) - CASCADE on delete
    # price: float
    # user_id: foreign key (users) CASCADE on delete
    # condition: choices
    # set: charfield
    # localization: choices (countries)
    # amount of cards: integer > 0

# TODO create user profile model (one to one field with User)
    # username = models.charfield(validation)
    # email = models.charfield
    # password = models.charfield (encrypted data?)
    # bio = models.textfield


class UserAddress(models.Model):
    country = models.CharField(max_length=100, verbose_name='Country')
    state_province = models.CharField(max_length=100, verbose_name='State/Province')
    city = models.CharField(max_length=100, verbose_name='City')
    street = models.CharField(max_length=100, verbose_name='Street')
    zip_code = models.CharField(max_length=10, verbose_name='Zip Code')

class UserProfile(models.Model):
    user_name = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Username')
    user_email = models.EmailField(max_length=254, verbose_name='E-mail')
    user_full_name = models.CharField(max_length=254, default='name', verbose_name = 'Full name')
    user_sales = models.IntegerField(null=False, blank=False, default=0, verbose_name='Sales Amount')
    user_address = models.ForeignKey(UserAddress, on_delete=models.CASCADE)

