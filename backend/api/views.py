from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serialisers import ProductSerialiser

# django rest framework view
@api_view(["POST"])
def api_home(request, *args, **kwargs): # request -> HttpRequest class instance from django

    serialiser = ProductSerialiser(data=request.data)
    if serialiser.is_valid(raise_exception=True):
        instance = serialiser.save()
        print(instance)
        data = serialiser.data
    return Response(data)