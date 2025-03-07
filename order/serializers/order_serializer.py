from rest_framework import serializers

from product.models import Product
from product.serializers.product_serializer import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=True, many=False)
    total = serializers.SerializerMethodField()

    def get_total(self, instace):
        total = sum([product.price for product in instace.product.all()])
        return total

    class Meta:
        model = Product
        fields = ['product', 'total']