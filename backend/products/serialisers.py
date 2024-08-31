from rest_framework import serializers

from .models import Product

class ProductSerialiser(serializers.ModelSerializer):
    # enrich serialiser with other values
    discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        # fields = '__all__'
        fields = [
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