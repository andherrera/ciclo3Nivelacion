from rest_framework import generics, status
from rest_framework.response import Response
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from invoiceApp.serializers.clienteSerializer import ClienteSerializer
from invoiceApp.serializers.usuarioSerializer import UsuarioSerializer
from invoiceApp.models.cliente import Cliente


class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
        print("GET a todos los clientes")
        queryset = self.get_queryset()
        serializer = ClienteSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print("POST a Cliente")
        usuarioData = request.data.pop('user')
        serializerU  = UsuarioSerializer(data=usuarioData)
        serializerU.is_valid(raise_exception=True)
        usuario = serializerU.save()
        enfData = request.data   
        enfData.update({"user":usuario.id})
        serializerEnf = ClienteSerializer(data=enfData)
        serializerEnf.is_valid(raise_exception=True)
        serializerEnf.save()
        return Response(status=status.HTTP_201_CREATED)

        """ tokenData = {
                     "username":request.data["username"],
                     "password":request.data["password"]
                    }
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED) """

        