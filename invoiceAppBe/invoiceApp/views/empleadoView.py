from rest_framework import generics, status
from rest_framework.response import Response
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from invoiceApp.serializers.empleadoSerializer import EmpleadoSerializer
from invoiceApp.serializers.usuarioSerializer import UsuarioSerializer
from invoiceApp.models.empleado import Empleado


class EmpleadoListCreateView(generics.ListCreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
        print("GET a todos los empleados")
        queryset = self.get_queryset()
        serializer = EmpleadoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print("POST Empleado")
        usuarioData = request.data.pop('user')
        usuarioData.update({"rol": "Empleado"})
        serializerU  = UsuarioSerializer(data=usuarioData)
        serializerU.is_valid(raise_exception=True)
        usuario = serializerU.save()
        enfData = request.data   
        enfData.update({"user":usuario.id})
        serializerEnf = EmpleadoSerializer(data=enfData)
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

class EmpleadoRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    lookup_field = "id"             # campo con el que se realiza la búsqueda de los objetos
    lookup_url_kwarg = 'pk'         # nombre dado en la url al argumento
    #permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        print("GET a empleado")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print("PUT a empleado")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().put(request, *args, **kwargs)

        