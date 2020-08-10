from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ClienteForm, ProductoForm
from .models import Cliente, Factura, Producto
# Create your views here.
def menu(request):
    opciones = {'Menu': 'Menu Principal',
                'Cliente': 'Clientes','Producto':'Productos','Factura':'Ventas'}

    return render(request, 'principal.html', opciones)

#CLIENTE

def cliente(request):
    opciones = {'Menu': 'Menu Principal',
                'Cliente': 'Clientes','Producto':'Productos','Factura':'Ventas', 'accion': 'Crear'}
    # return HttpResponse('Contacto')
    if request.method == 'POST':
        # pass
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarcliente')
    else:
        form = ClienteForm()
        opciones['form'] = form

    return render(request, 'cliente.html', opciones)


def editarCliente(request, id):
    opciones = {'Menu': 'Menu Principal',
                'Cliente': 'Clientes','Producto':'Productos','Factura':'Ventas', 'accion': 'Actualizar'}
    cliente = Cliente.objects.get(id=id)
    if request.method == 'GET':
        form = ClienteForm(instance=cliente)
        opciones['form'] = form
    else:
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listarcliente')

    return render(request, 'cliente.html', opciones)


def listarCliente(request):
    cliente = Cliente.objects.all()
    opciones = {'Menu': 'Menu Principal',
                'Cliente': 'Clientes','Producto':'Productos','Factura':'Ventas',  'clientes': cliente}
    return render(request, 'listar_cliente.html', opciones)


def eliminarCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listarcliente')
    return render(request, 'eliminar_Cliente.html', {'cliente': cliente})

# PRODUCTO

def producto(request):
    opciones = {'Menu': 'Menu Principal',
                'Cliente': 'Clientes','Producto':'Productos','Factura':'Ventas', 'accion': 'Crear'}
    # return HttpResponse('Contacto')
    if request.method == 'POST':
        # pass
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarproducto')
    else:
        form = ProductoForm()
        opciones['form'] = form

    return render(request, 'producto.html', opciones)


def editarProducto(request, id):
    opciones = {'Menu': 'Menu Principal',
                'Cliente': 'Clientes','Producto':'Productos','Factura':'Ventas', 'accion': 'Actualizar'}
    producto = Producto.objects.get(id=id)
    if request.method == 'GET':
        form = ProductoForm(instance=producto)
        opciones['form'] = form
    else:
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listarproducto')

    return render(request, 'producto.html', opciones)


def listarProducto(request):
    producto = Producto.objects.all()
    opciones = {'Menu': 'Menu Principal',
                'Cliente': 'Clientes','Producto':'Productos','Factura':'Ventas', 'productos': producto}
    return render(request, 'listar_producto.html', opciones)


def eliminarProducto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listarproducto')
    return render(request, 'eliminar_producto.html', {'producto': producto})

#FACTURA
def listarFactura(request):
    factura = Factura.objects.all()
    opciones = {'Menu': 'Menu Principal',
                'Cliente': 'Clientes','Producto':'Productos','Factura':'Ventas', 'facturas': factura}
    return render(request, 'listar_factura.html', opciones)