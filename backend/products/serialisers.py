from rest_framework import serializers

from .models import Product
from . import validators

class ProductSerialiser(serializers.ModelSerializer):
    # enrich serialiser with other values
    discount = serializers.SerializerMethodField(read_only=True)
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
            'url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'discount'
        ]

    def get_discount(self, class_instance):

        if not isinstance(class_instance, Product):
            return None
        return class_instance.get_discount()