from rest_framework import status, views
from rest_framework.response import Response
from invoiceApp.models.producto import Producto
from invoiceApp.models.compra import Compra
from invoiceApp.serializers.compraSerializer import CompraSerializer
from invoiceApp.serializers.productoSerializer import ProductoSerializer
from invoiceApp.models.factura import Factura
from invoiceApp.serializers.facturaSerializer import FacturaSerializer
from django.http.response import JsonResponse

class CompraCreateView(views.APIView):
    def post(self, request):
        data = request.data
        productoCantidad = data['cantidad']
        productoKey = data['producto']
        facturaKey = data['factura']        
        productModel = Producto.objects.get(pk=productoKey)
        serializerP = ProductoSerializer(productModel)
        productData = serializerP.data
        productPrecio = productData['precioU']
        productTotalCost = productPrecio * productoCantidad
        data.update({"precioTotal": productTotalCost})
        facturaModel = Factura.objects.get(pk=facturaKey)
        serializerF = FacturaSerializer(facturaModel)
        facturaData = serializerF.data
        facturaCostoTotal = facturaData['costoTotal']
        facturaCostoTotal += productTotalCost
        facturaData.update({"costoTotal": facturaCostoTotal})
        serializerF=FacturaSerializer(facturaModel, data=facturaData)
        serializerC=CompraSerializer(data=data)
        if serializerF.is_valid() and serializerC.is_valid():
            serializerF.save()
            serializerC.save()
            return Response(serializerC.data,status=status.HTTP_201_CREATED)
        #datos = {'message' : "Success"}
        #return JsonResponse(datos) 
        return Response(serializerC.errors,status=status.HTTP_400_BAD_REQUEST)