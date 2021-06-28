from rest_framework import serializers
from .models import Brand, Item, Order


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand

        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item

        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order

        fields = '__all__'
