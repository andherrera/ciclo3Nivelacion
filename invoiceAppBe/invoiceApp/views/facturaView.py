from rest_framework import status
from rest_framework.response import Response
from invoiceApp.models.factura import Factura
from invoiceApp.serializers.facturaSerializer import FacturaSerializer
from rest_framework.decorators import api_view


@api_view(['GET','POST'])
def facturaListCreate(request):
    if request.method == 'GET':
        modelo=Factura.objects.all()
        serializer=FacturaSerializer(modelo, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=FacturaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

@api_view(['PUT','DELETE'])
def facturaRetrieveDelete(request,pk):
    if request.method =='PUT':
        modelo=Factura.objects.get(pk=pk)
        serializer=FacturaSerializer(modelo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    elif request.method == 'DELETE':
        modelo=Factura.objects.get(pk=pk)
        modelo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
