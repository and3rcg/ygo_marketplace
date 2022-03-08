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


    user_id = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='User ID')
    card_id = models.ForeignKey(CardModel, on_delete=models.CASCADE, verbose_name='Card ID')
    price = models.FloatField(null=False, blank=False, default=1, verbose_name='Price', validators=[MinValueValidator(1)])
    card_set = models.CharField(max_length=20,null=False, blank=False, default="XXXX-000", verbose_name="Set")
    card_rarity = models.CharField(max_length=40,null=False, blank=False, default="rare", verbose_name="Rarity")
    card_amount = models.IntegerField(validators=[MinValueValidator(1)])
    card_region = models.CharField(max_length=20, choices=localization_choices)
    card_condition = models.CharField(max_length=20, choices=condition_choices)

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
    
