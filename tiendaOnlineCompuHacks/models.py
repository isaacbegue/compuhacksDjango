from django.db import models
from django.contrib.auth.models import User


class Domicilio(models.Model):
    direccion_id = models.AutoField(primary_key=True)
    calle_numero = models.CharField(max_length=100, null=True)
    ciudad = models.CharField(max_length=50, null=True)
    estado_provincia = models.CharField(max_length=50, null=True)
    pais = models.CharField(max_length=50, null=True)
    codigo_postal = models.CharField(max_length=20, null=True)
    
class Empleado(models.Model):
    empleado_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    puesto = models.CharField(max_length=45, null=True)
    area_trabajo = models.CharField(max_length=45, null=True)
    permisos_acceso = models.CharField(max_length=45, null=True)
    direccion = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)
    empleadoscol = models.CharField(max_length=45, null=True)

class MetodoPago(models.Model):
    metodo_pago_id = models.AutoField(primary_key=True)
    nombre_metodo_pago = models.CharField(max_length=45, null=True)
    descripcion = models.TextField(null=True)

class Cliente(models.Model):
    cliente_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    fecha_registro = models.DateField(null=True)
    metodo_pago_predeterminado = models.ForeignKey(MetodoPago, on_delete=models.SET_NULL, null=True, related_name='+')
    direccion_predeterminada = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True, related_name='+')

class Proveedor(models.Model):
    proveedor_id = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    telefono = models.CharField(max_length=20, null=True)
    direccion = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)

class CategoriaProducto(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=50, null=True)

class Producto(models.Model):
    producto_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=True)
    descripcion = models.TextField(null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    cantidad_inventario = models.IntegerField(null=True)
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.SET_NULL, null=True)

class PedidoCliente(models.Model):
    pedido_id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    fecha_pedido = models.DateField(null=True)
    estado_pedido = models.CharField(max_length=45, null=True)

class DetallePedido(models.Model):
    detalle_pedido_id = models.AutoField(primary_key=True)
    pedido = models.ForeignKey(PedidoCliente, on_delete=models.CASCADE, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(null=True)

class Factura(models.Model):
    factura_id = models.AutoField(primary_key=True)
    pedido = models.ForeignKey(PedidoCliente, on_delete=models.CASCADE)
    fecha_emision = models.DateField(null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True)

class PedidoProveedor(models.Model):
    pedido_proveedores_ID = models.AutoField(primary_key=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio_por_unidad = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    fecha_de_compra = models.DateField(null=True)
    pedido_entregado = models.BooleanField(null=True)
    pedido_pagado = models.BooleanField(null=True)
    cantidad_comprada = models.IntegerField(null=True)


