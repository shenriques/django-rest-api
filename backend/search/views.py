from django.shortcuts import render
from rest_framework import generics
from products.models import Product
from products.serialisers import ProductSerialiser

class SearchListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialiser

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        # by default, search result is none (havent searched yet)
        results = Product.objects.none()
        # if query result is not none
        if q is not None:
            user = None # by default, no user 

            if self.request.user.is_authenticated:
                user = self.request.user

            results = queryset.search(q, user=user)
        return results
