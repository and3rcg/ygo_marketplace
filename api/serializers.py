from djoser.serializers import UserCreateSerializer, UserSerializer
from djoser.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers

from api.models import CardModel, CardOnSale

User = get_user_model()

class RegisterSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'password', 'email']
        
    def create(self, validated_data):
        """
        customizing the create method to encrypt the passwords
        """
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class MyUserSerializer(UserSerializer):
    # Customize the data provided by the /users/me/ endpoint:
    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            settings.USER_ID_FIELD,
            settings.LOGIN_FIELD,
            'bio',
        )
        read_only_fields = (settings.LOGIN_FIELD,)


class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CardModel
        fields = ['url', 'name', 'type', 'description', 'image_url']


class CardOnSaleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CardOnSale