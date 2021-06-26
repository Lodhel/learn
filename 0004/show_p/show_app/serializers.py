from rest_framework import serializers
from . import models


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brand

        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item

        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order

        fields = '__all__'
