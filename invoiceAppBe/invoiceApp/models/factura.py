from django.db import models
from .cliente import Cliente

class Factura(models.Model):
    id = models.AutoField(primary_key=True)    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    mPago = models.CharField('mPago', max_length = 30)
    costoTotal = models.FloatField(default=0)