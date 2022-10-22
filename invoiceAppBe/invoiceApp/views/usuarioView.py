from rest_framework import status, views
from rest_framework.response import Response
from invoiceApp.models.user import User
from invoiceApp.serializers.usuarioSerializer import UsuarioSerializer

class UsuarioRetrieveUpdateDeleteView(views.APIView):

    def get(self, request, pk, format=None):
        model=User.objects.get(pk=pk)
        serializer=UsuarioSerializer(model)
        return Response(serializer.data)