from django.db import models
from .empleado import Empleado

class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    nombre = models.CharField('nombre', max_length = 30)
    fecha = models.CharField('fecha', max_length = 30)