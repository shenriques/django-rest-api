from rest_framework import viewsets

from .models import Product
from .serialisers import ProductSerialiser

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerialiser
    lookup_field = 'pk'
