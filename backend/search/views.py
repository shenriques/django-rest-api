from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from products.models import Product
from products.serialisers import ProductSerialiser

from . import client

class SearchListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        user = None
        if request.user.is_authenticated:
            user = request.user.username

        query = request.GET.get('q')
        public = str(request.GET.get('public')) != "0"
        tag = request.GET.get('tag') or None
        if not query:
            return Response('', status=400)
        results = client.perform_search(query, tags=tag, user=user, public=public)
        return Response(results)

class SearchListOldView(generics.ListAPIView):
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
