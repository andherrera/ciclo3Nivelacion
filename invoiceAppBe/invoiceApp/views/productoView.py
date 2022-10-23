from rest_framework import status, views
from rest_framework.response import Response
from invoiceApp.models.producto import Producto
from invoiceApp.serializers.productoSerializer import ProductoSerializer

class ProductoCreateView(views.APIView):
    def post(self, request):        
        serializar=ProductoSerializer(data=request.data)
        if serializar.is_valid():
            serializar.save()
            return Response(serializar.data,status=status.HTTP_201_CREATED)
        return Response(serializar.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        modelo=Producto.objects.all()
        serializer=ProductoSerializer(modelo, many=True)
        return Response(serializer.data)

class ProductoRetrieveUpdateDeleteView(views.APIView):

    def get(self, request, pk, format=None):
        model=Producto.objects.get(pk=pk)
        serializer=ProductoSerializer(model)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        model=Producto.objects.get(pk=pk)
        serializer=ProductoSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        modelo=Producto.objects.get(pk=pk)
        modelo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)