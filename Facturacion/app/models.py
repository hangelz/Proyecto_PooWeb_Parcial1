from django.db import models

# Create your models here.
class Producto(models.Model):
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField(default=0)
    stock = models.FloatField(default=0)
    iva = models.BooleanField(default=True)

    def __str__(self):
        return '%s, %s'% (self.descripcion, self.precio)

class Cliente(models.Model):
    ruc = models.CharField(max_length=13)
    nombre = models.CharField(max_length=300)
    direccion = models.TextField(blank=True, null=True)
    producto = models.ManyToManyField(Producto)
    
    def __str__(self):
        return '%s, %s'% (self.ruc, self.nombre)

class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    fecha = models.DateField()
    total = models.FloatField(default=0)

    def __str__(self):
        return '%s, %s, %s'% (self.cliente, self.fecha, self.total)

class DetalleFactura(models.Model):
    factura=models.ForeignKey(Factura, on_delete= models.CASCADE)
    producto=models.ForeignKey(Producto, on_delete= models.CASCADE)
    cantidad = models.FloatField(default=0)
    precio = models.FloatField(default=0)
    subtotal = models.FloatField(default=0)

    def __str__(self):
        return '%s, %s, %s'% (self.factura, self.producto, self.cantidad)