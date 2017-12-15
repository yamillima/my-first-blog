from django.db import models
from django.utils import timezone
import datetime

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='tienda/productos')
    precio = models.IntegerField()
    descripcion = models.TextField(blank=True)
    para_mujer = models.BooleanField(default=True)
    para_hombre = models.BooleanField(default=False)
    para_chicos = models.BooleanField(default=False)
    abierto_desde_las = models.TimeField()
    cierra_a_las = models.TimeField()

class Visita(models.Model):
    fecha = models.DateTimeField(default=datetime.datetime.now())

class Dama(models.Model):
    fecha = models.DateTimeField(default=datetime.datetime.now())

class Hombre(models.Model):
    fecha = models.DateTimeField(default=datetime.datetime.now())

class Chico(models.Model):
    fecha = models.DateTimeField(default=datetime.datetime.now())
