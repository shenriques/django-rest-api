from rest_framework import generics

from .models import Product
from .serialisers import ProductSerialiser

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialiser

    # method for overriding object save / deletion behaviour
    def perform_create(self, serializer):

        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        # if user doesnt provide content for new object, set it to be the title
        if content is None:
            content = title

        serializer.save(content=content)

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    # has to be serializer not serialiser!!!
    serializer_class = ProductSerialiser