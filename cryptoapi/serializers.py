from rest_framework import serializers
from .models import Cryptocurrency

class CryptocurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = ['id', 'name', 'symbol', 'price', 'timestamp']

class CryptocurrencyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = ['name', 'symbol', 'price', 'timestamp']
