from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serialisers import ProductSerialiser

# django rest framework view
@api_view(["GET"])
def api_home(request, *args, **kwargs): # request -> HttpRequest class instance from django

    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerialiser(instance).data
    return Response(data)