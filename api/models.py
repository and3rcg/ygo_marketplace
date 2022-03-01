from django.db import models

# Create your models here.

class CardModel(models.Model):
    card_name = models.CharField(max_length=100, null=False, blank=False, default='name', verbose_name="Name")
    card_attribute = models.CharField(max_length=20, null=True, blank=True, verbose_name="Attribute")
    card_race = models.CharField(max_length=20, null=False, blank=False, default='race', verbose_name="Class")
    card_level = models.IntegerField(null=True, blank=True, verbose_name="Level/Rank/Link")
    card_atk = models.IntegerField(null=True, blank=True, verbose_name="ATK")
    card_def = models.IntegerField(null=True, blank=True, verbose_name="DEF")
    card_description = models.TextField(null=False, blank=False, default='desc', verbose_name="Effect/Description")
    card_type = models.CharField(max_length=100, null=False, blank=False, default='type', verbose_name="Type")

# create class for card to sell, that includes the set's code and rarity
