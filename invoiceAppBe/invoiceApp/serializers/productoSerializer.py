from rest_framework import serializers
from invoiceApp.models.producto import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'