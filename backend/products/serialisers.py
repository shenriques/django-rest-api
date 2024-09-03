from rest_framework import serializers

from api.serialisers import UserPublicSerialiser

from .models import Product
from . import validators

class ProductInlineSerialiser(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk', read_only=True)
    title = serializers.CharField(read_only=True)

class ProductSerialiser(serializers.ModelSerializer):
    # enrich serialiser with other values
    owner = UserPublicSerialiser(source='user', read_only=True)

    # add clickable url for each product (only works on model serialiser)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')

    # validate the title field
    title = serializers.CharField(validators=[validators.validate_title_no_hello, validators.unique_product_title])

    # can use foreign key relationships (i.e if there was a user attached to the product model)
    # e.g. owner = serializers.CharField(source=user.email, read_only=True), then add to Meta fields
    class Meta:
        model = Product
        # fields = '__all__'
        fields = [
            'owner',
            'url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price'
        ]

    def get_discount(self, class_instance):

        if not isinstance(class_instance, Product):
            return None
        return class_instance.get_discount()