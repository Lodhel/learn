from rest_framework import viewsets

from . import serializers
from . import models


class BrandViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BrandSerializer
    queryset = models.Brand.objects.all()


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ItemSerializer
    queryset = models.Item.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all()
