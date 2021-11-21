from datetime import time
from rest_framework import serializers
from api.models import *


class CitySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = CityModel
        fields = ['id', 'name']


class StreetSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = StreetModel
        fields = ['id', 'name', 'city']


class ShopSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    open = serializers.IntegerField(source='isOpen', read_only=True)
    open_time = serializers.TimeField(default=time(8), initial=time(8))
    close_time = serializers.TimeField(default=time(20), initial=time(20))
    city = serializers.SlugRelatedField(slug_field='name', queryset=CityModel.objects.all())
    street = serializers.SlugRelatedField(slug_field='name', queryset=StreetModel.objects.all())

    class Meta:
        model = ShopModel
        fields = ['id' ,'name', 'city', 'street', 'building', 'open', 'open_time', 'close_time']
