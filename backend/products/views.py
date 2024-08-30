from rest_framework import generics

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

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

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialiser
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    # has to be serializer not serialiser!!!
    serializer_class = ProductSerialiser

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        # if theres a pk, its one object, you want to see its details
        if pk is not None:
            product = get_object_or_404(Product, pk=pk)
            data = ProductSerialiser(product).data
            return Response(data)
        # if theres no pk, its multiple object, list them
        queryset = Product.objects.all()
        data = ProductSerialiser(queryset, many=True).data # serializing multiple objects
        return Response(data)
    
    if method == 'POST':
        serializer = ProductSerialiser(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            # if user doesnt provide content for new object, set it to be the title
            if content is None:
                content = title
                serializer.save(content=content)
        return Response({"invalid": "data"}, status=400)