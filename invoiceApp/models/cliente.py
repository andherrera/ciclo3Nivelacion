from msvcrt import open_osfhandle
from django.db import models
from .user import User

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField('Email', max_length = 100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
