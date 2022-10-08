from rest_framework import serializers
from invoiceApp.models.cliente import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['email', 'user']