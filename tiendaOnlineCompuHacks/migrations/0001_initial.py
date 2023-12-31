# Generated by Django 4.0.5 on 2023-09-08 21:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('categoria_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_categoria', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cliente_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('fecha_registro', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('direccion_id', models.AutoField(primary_key=True, serialize=False)),
                ('calle_numero', models.CharField(max_length=100, null=True)),
                ('ciudad', models.CharField(max_length=50, null=True)),
                ('estado_provincia', models.CharField(max_length=50, null=True)),
                ('pais', models.CharField(max_length=50, null=True)),
                ('codigo_postal', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MetodoPago',
            fields=[
                ('metodo_pago_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_metodo_pago', models.CharField(max_length=45, null=True)),
                ('descripcion', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('proveedor_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_empresa', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('telefono', models.CharField(max_length=20, null=True)),
                ('direccion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tiendaOnlineCompuHacks.domicilio')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('producto_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('descripcion', models.TextField(null=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('cantidad_inventario', models.IntegerField(null=True)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tiendaOnlineCompuHacks.categoriaproducto')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoProveedor',
            fields=[
                ('pedido_proveedores_ID', models.AutoField(primary_key=True, serialize=False)),
                ('precio_por_unidad', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('fecha_de_compra', models.DateField(null=True)),
                ('pedido_entregado', models.BooleanField(null=True)),
                ('pedido_pagado', models.BooleanField(null=True)),
                ('cantidad_comprada', models.IntegerField(null=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendaOnlineCompuHacks.producto')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendaOnlineCompuHacks.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoCliente',
            fields=[
                ('pedido_id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_pedido', models.DateField(null=True)),
                ('estado_pedido', models.CharField(max_length=45, null=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tiendaOnlineCompuHacks.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('factura_id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_emision', models.DateField(null=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendaOnlineCompuHacks.pedidocliente')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('empleado_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('puesto', models.CharField(max_length=45, null=True)),
                ('area_trabajo', models.CharField(max_length=45, null=True)),
                ('permisos_acceso', models.CharField(max_length=45, null=True)),
                ('empleadoscol', models.CharField(max_length=45, null=True)),
                ('direccion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tiendaOnlineCompuHacks.domicilio')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('detalle_pedido_id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(null=True)),
                ('pedido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tiendaOnlineCompuHacks.pedidocliente')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tiendaOnlineCompuHacks.producto')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='direccion_predeterminada',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='tiendaOnlineCompuHacks.domicilio'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='metodo_pago_predeterminado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='tiendaOnlineCompuHacks.metodopago'),
        ),
    ]
