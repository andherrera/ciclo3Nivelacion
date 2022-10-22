from rest_framework import serializers
from invoiceApp.models.empleado import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ['contrato', 'area', 'user']