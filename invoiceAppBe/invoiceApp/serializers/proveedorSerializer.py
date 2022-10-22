from rest_framework import serializers
from invoiceApp.models.proveedor import Proveedor

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'fecha', 'empleado']