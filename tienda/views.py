from django.views import generic
from .models import Tendero, Producto, Visita, Dama, Hombre, Chico, Compra, ComprarClick
from .forms import CompraForm, ComentarioForm
from django.utils import timezone
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.mail import send_mail
import datetime

class BackDoorView(generic.ListView):
    template_name = 'tienda/index.html'

    def get_queryset(self):
        return Tendero.objects.all()

class IndexView(generic.ListView):
    template_name = 'tienda/index.html'

    def get_queryset(self):
        now = datetime.datetime.now()
        visita = Visita.objects.create()
        visita.fecha = now
        visita.save()
        return Tendero.objects.all()

class DamaView(generic.ListView):
    template_name = 'tienda/mujer.html'

    def get_queryset(self):
        now = datetime.datetime.now()
        dama = Dama.objects.create()
        dama.fecha = now
        dama.save()
        return Tendero.objects.all()

class HombreView(generic.ListView):
    template_name = 'tienda/hombre.html'

    def get_queryset(self):
        now = datetime.datetime.now()
        hombre = Hombre.objects.create()
        hombre.fecha = now
        hombre.save()
        return Tendero.objects.all()

class ChicoView(generic.ListView):
    template_name = 'tienda/chicos.html'

    def get_queryset(self):
        now = datetime.datetime.now()
        chico = Chico.objects.create()
        chico.fecha = now
        chico.save()
        return Tendero.objects.all()

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

    def form_valid(self, form, **kwargs):
        comprador = form.cleaned_data['nombre_del_comprador']
        telefono = form.cleaned_data['telefono_del_comprador']
        precio = form.cleaned_data['precio']
        destinatario = form.cleaned_data['nombre_del_destinatario']
        direccion = form.cleaned_data['direccion_de_entrega']
        fecha = form.cleaned_data['fecha_de_entrega'].strftime('%b %d de %Y')
        hora = form.cleaned_data['hora_de_entrega'].strftime('%I:%M %p')
        mail_to = Producto.objects.get(pk=self.kwargs['pk']).vendedor.email
        msg = 'Vendiste -' + Producto.objects.get(pk=self.kwargs['pk']).nombre + '- en Gugif. Precio: ' + precio +  '. Comprador: ' + comprador + '. Teléfono: ' + telefono + '. Destinatario: ' + destinatario + '. Dirección de entrega: ' + direccion + '. Fecha y hora de entrega: ' + fecha + ' a las ' + hora
        html_message = 'Vendiste <b>' + Producto.objects.get(pk=self.kwargs['pk']).nombre + '</b> en Gugif. <br><b>Precio:</b> ' + precio +  '. <br><b>Comprador:</b> ' + comprador + '. <br><b>Teléfono:</b> ' + telefono + '. <br><b>Destinatario:</b> ' + destinatario + '. <br><b>Dirección de entrega:</b> ' + direccion + '. <br><b>Fecha y hora de entrega:</b> ' + fecha + ' a las ' + hora
        send_mail('¡Tienes una venta!', msg, 'Gugif <info@gugif.com>', [mail_to], html_message=html_message)
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
