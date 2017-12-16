from django.views import generic
from .models import Producto, Visita, Dama, Hombre, Chico, Compra
import datetime

class IndexView(generic.ListView):
    template_name = 'tienda/index.html'

    def get_queryset(self):
        return Producto.objects.all()

class FacebookView(generic.ListView):
    template_name = 'tienda/index.html'

    def get_queryset(self):
        now = datetime.datetime.now()
        visita = Visita.objects.create()
        visita.fecha = now
        visita.save()
        return Producto.objects.all()

class DamaView(generic.ListView):
    template_name = 'tienda/mujer.html'

    def get_queryset(self):
        now = datetime.datetime.now()
        dama = Dama.objects.create()
        dama.fecha = now
        dama.save()
        return Producto.objects.filter(para_mujer=True)

class HombreView(generic.ListView):
    template_name = 'tienda/hombre.html'

    def get_queryset(self):
        now = datetime.datetime.now()
        hombre = Hombre.objects.create()
        hombre.fecha = now
        hombre.save()
        return Producto.objects.filter(para_hombre=True)

class ChicoView(generic.ListView):
    template_name = 'tienda/chicos.html'

    def get_queryset(self):
        now = datetime.datetime.now()
        chico = Chico.objects.create()
        chico.fecha = now
        chico.save()
        return Producto.objects.filter(para_chicos=True)

class ComprarView(generic.ListView):
    template_name = 'tienda/comprar.html'

    def get_queryset(self):
        now = datetime.datetime.now()
        compra = Compra.objects.create()
        compra.fecha = now
        compra.save()
        return Producto.objects.all()
