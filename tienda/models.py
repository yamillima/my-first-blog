from django.db import models
from django.utils import timezone
import datetime

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='tienda/productos')
    precio = models.IntegerField()
    descripción = models.TextField(blank=True)
    para_mujer = models.BooleanField(default=True)
    para_hombre = models.BooleanField(default=False)
    para_niños = models.BooleanField(default=False)
    abierto_desde_las = models.TimeField()
    cierra_a_las = models.TimeField()

    def __str__(self):
        return self.nombre

    def precio_millar(self):
        return '{:,}'.format(self.precio).replace(',', ' ')

    def estado(self):
        if self.abierto_desde_las < datetime.datetime.now().time() < self.cierra_a_las:
            return "ABIERTO"
        else:
            return "CERRADO"

class Visita(models.Model):
    fecha = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return timezone.localtime(self.fecha).strftime('%b. %d de %Y - %I:%M:%S %p')

class Dama(models.Model):
    fecha = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return timezone.localtime(self.fecha).strftime('%b. %d de %Y - %I:%M:%S %p')

class Hombre(models.Model):
    fecha = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return timezone.localtime(self.fecha).strftime('%b. %d de %Y - %I:%M:%S %p')

class Chico(models.Model):
    fecha = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return timezone.localtime(self.fecha).strftime('%b. %d de %Y - %I:%M:%S %p')
