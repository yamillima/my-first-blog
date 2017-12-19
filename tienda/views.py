from django.views import generic
from .models import Producto, Visita, Dama, Hombre, Chico, Compra, ComprarClick
from .forms import CompraForm, ComentarioForm
from django.utils import timezone
from django.shortcuts import redirect
from django.http import HttpResponse
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

class ComprarView(generic.edit.FormView):
    template_name = 'tienda/compra.html'
    form_class = CompraForm
    success_url = 'pedido'

    def get_initial(self, **kwargs):
        initial = super(ComprarView, self).get_initial()
        initial['regalo'] = Producto.objects.get(pk=self.kwargs['pk']).nombre
        initial['precio'] = Producto.objects.get(pk=self.kwargs['pk']).precio_millar
        comprarclick = ComprarClick.objects.create()
        comprarclick.fecha = timezone.now()
        comprarclick.producto = Producto.objects.get(pk=self.kwargs['pk']).nombre
        comprarclick.save()
        return initial

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ComentarioView(generic.edit.FormView):
    template_name = 'tienda/opiniones.html'
    form_class = ComentarioForm
    success_url = 'gracias'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class GraciasView(generic.ListView):
    template_name = 'tienda/gracias.html'
    queryset = Producto.objects.all()

class PedidoView(generic.ListView):
    template_name = 'tienda/pedido.html'
    queryset = Producto.objects.all()
