from rest_framework import serializers
from invoiceApp.models.cliente import User

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'name', 'lastname', 'rol', 'email', 'city', 'address', 'cellphone']