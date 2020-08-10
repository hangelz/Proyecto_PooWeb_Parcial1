from django import forms
from .models import Cliente, Factura, Producto


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('ruc', 'nombre', 'direccion')
        label = {'ruc': 'Ruc', 'nombre': 'Nombre', 'direccion': 'Direccion'}

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('descripcion', 'precio', 'stock', 'iva')
        label = {'descripcion': 'Descripcion', 'precio': 'Precio', 'stock': 'Stock','iva': 'Iva'}

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ('cliente', 'fecha', 'total')
        label = {'cliente': 'Cliente', 'fecha': 'Fecha', 'total': 'Total'}