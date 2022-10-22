from django.db import models
from .proveedor import Proveedor

class Producto(models.Model):
    id = models.AutoField(primary_key=True)    
    nombre = models.CharField('nombre', max_length = 30)    
    cantidad = models.IntegerField()
    pais = models.CharField('pais', max_length = 30)
    precioU = models.FloatField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)