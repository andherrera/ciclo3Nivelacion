from unittest.util import _MAX_LENGTH
from django.db import models
from .user import User

class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contrato = models.CharField('contrato', max_length = 30)
    area = models.CharField('area', max_length = 30)