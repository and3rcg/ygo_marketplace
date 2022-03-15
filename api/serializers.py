from rest_framework import serializers

from api.models import CardModel, User

class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CardModel
        fields = ['url', 'name', 'type', 'description']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name', 'password', 'email']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
        }
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


# TODO remove this when done tinkering with axios
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name', 'password', 'email']
        
