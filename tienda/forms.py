from django import forms

from .models import Compra, Producto

from django.utils import timezone

class CompraForm(forms.ModelForm):

    class Meta():
        model = Compra
        fields = ('regalo', 'precio', 'telefono_del_comprador', 'nombre_del_comprador', 'nombre_del_destinatario', 'direccion_de_entrega', 'fecha_de_entrega', 'hora_de_entrega',)
        widgets = {
            'regalo': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'precio': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'telefono_del_comprador': forms.NumberInput(attrs={'class': 'form-control gugif'}),
            'nombre_del_comprador': forms.TextInput(attrs={'class': 'form-control gugif'}),
            'nombre_del_destinatario': forms.TextInput(attrs={'class': 'form-control gugif'}),
            'direccion_de_entrega': forms.TextInput(attrs={'class': 'form-control gugif'}),
            'fecha_de_entrega': forms.DateInput(attrs={'type': 'date', 'class': 'form-control gugif'}),
            'hora_de_entrega': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control gugif'}),
        }
