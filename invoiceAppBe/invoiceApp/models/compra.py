from django.db import models
from .factura import Factura
from .producto import Producto

class Compra(models.Model):    
    factura=models.ForeignKey(Factura, on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precioTotal = models.FloatField()