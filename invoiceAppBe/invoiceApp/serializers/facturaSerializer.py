from rest_framework import serializers
from invoiceApp.models.factura import Factura

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'