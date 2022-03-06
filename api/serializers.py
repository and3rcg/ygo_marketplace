from rest_framework import serializers

from api.models import CardModel

class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CardModel
        fields = ['url', 'card_name', 'card_type', 'card_description']
