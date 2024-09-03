from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product

# example of applying custom validation checks
def validate_title_no_hello(value):
    if 'hello' in value.lower():
        raise serializers.ValidationError(f"{value} is not allowed")
    return value

# iexact = case insensitive
unique_product_title = UniqueValidator(queryset=Product.objects.all(), lookup='iexact')