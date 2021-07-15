
from rest_framework import viewsets

from .serializers import ProductSerializer, TypeSerializer, PriceSerializer

from .models import Product, Type, Price


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all().order_by('name')
    serializer_class = TypeSerializer


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all().order_by('currency')
    serializer_class = PriceSerializer



