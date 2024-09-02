from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product

def validate_title_no_hello(value):
    if 'hello' in value.lower():
        raise serializers.ValidationError("Can't put hello in the title")
    return value

unique_product_title = UniqueValidator(queryset=Product.objects.all())