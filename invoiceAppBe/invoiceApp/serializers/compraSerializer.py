from string import printable
from rest_framework import serializers
from invoiceApp.models.compra import Compra

class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__'