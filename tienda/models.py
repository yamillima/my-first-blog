from django.db import models
from django.utils import timezone
from django import forms
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

    def __str__(self):
        return self.nombre

    def precio_millar(self):
        return "{:,}".format(self.precio).replace(',','.')

class Visita(models.Model):
    fecha = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return timezone.localtime(self.fecha).strftime('%b %d de %Y - %I:%M:%S %p')

class Dama(models.Model):
    fecha = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return timezone.localtime(self.fecha).strftime('%b %d de %Y - %I:%M:%S %p')

class Hombre(models.Model):
    fecha = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return timezone.localtime(self.fecha).strftime('%b %d de %Y - %I:%M:%S %p')

class Chico(models.Model):
    fecha = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return timezone.localtime(self.fecha).strftime('%b %d de %Y - %I:%M:%S %p')

class Compra(models.Model):
    fecha = models.DateTimeField(default=timezone.now)
    regalo = models.CharField(max_length=200)
    precio = models.CharField(max_length=200)
    telefono_del_comprador = models.CharField(max_length=200)
    nombre_del_comprador = models.CharField(max_length=200)
    nombre_del_destinatario = models.CharField(max_length=200)
    direccion_de_entrega = models.CharField(max_length=200)
    fecha_de_entrega = models.DateField()
    hora_de_entrega = models.TimeField()

    def __str__(self):
        return timezone.localtime(self.fecha).strftime('%b %d de %Y - %I:%M:%S %p')

class ComprarClick(models.Model):
    fecha = models.DateTimeField(default=timezone.now)
    producto = models.CharField(max_length=200, default='sin definir')

    def __str__(self):
        return timezone.localtime(self.fecha).strftime('%b %d de %Y - %I:%M:%S %p') + ' - ' + self.producto
