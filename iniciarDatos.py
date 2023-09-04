import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CompuHacks.settings')
django.setup()

import json
from tiendaOnlineCompuHacks.models import CategoriaProducto, Cliente, DetallePedido, Empleado, Factura, MetodoPago, PedidoCliente, PedidoProveedor, Producto, Domicilio, Proveedor
from django.contrib.auth.models import User

# Leer el archivo JSON
with open('productos.json') as f:
    productos_data = json.load(f)

# Crear categorias de producto
categorias = [
    'procesadores',
    'gabinetes',
    'tarjetas_madre',
    'tarjetas_de_video',
    'memorias_ram',
    'almacenamiento',
    'teclados',
    'ratones',
    'controles_para_videojuegos',
    'monitores',
    'ventiladores_y_enfriamiento',
    'audifonos_y_bocinas',
    'fuentes_de_alimentacion',
    'accesorios',
    'cables_y_adaptadores'
]

for categoria in categorias:
    CategoriaProducto.objects.create(nombre_categoria=categoria)

# Crear productos
for categoria, productos in productos_data.items():
    categoria_obj = CategoriaProducto.objects.get(nombre_categoria=categoria)
    for producto in productos:
        Producto.objects.create(
            nombre=producto['nombre'],
            descripcion=producto['descripcion'],
            precio=producto['precio'],
            cantidad_inventario=20,  # o cualquier otro valor
            categoria=categoria_obj,
        )

# Crear domicilios
domicilios = [
    {
        'calle_numero': '123 Calle Principal',
        'ciudad': 'Ciudad de México',
        'estado_provincia': 'Ciudad de México',
        'pais': 'México',
        'codigo_postal': '12345',
    },
    {
        'calle_numero': '456 Avenida Secundaria',
        'ciudad': 'Guadalajara',
        'estado_provincia': 'Jalisco',
        'pais': 'México',
        'codigo_postal': '67890',
    },
    {
        'calle_numero': '789 Calle Terciaria',
        'ciudad': 'Monterrey',
        'estado_provincia': 'Nuevo León',
        'pais': 'México',
        'codigo_postal': '11223',
    },
    {
        'calle_numero': '101 Calle Cuarta',
        'ciudad': 'Puebla',
        'estado_provincia': 'Puebla',
        'pais': 'México',
        'codigo_postal': '44556',
    },
    {
        'calle_numero': '121 Calle Quinta',
        'ciudad': 'Querétaro',
        'estado_provincia': 'Querétaro',
        'pais': 'México',
        'codigo_postal': '77889',
    },
    {
        'calle_numero': '141 Calle Sexta',
        'ciudad': 'Mérida',
        'estado_provincia': 'Yucatán',
        'pais': 'México',
        'codigo_postal': '99001',
    },
]

for domicilio in domicilios:
    Domicilio.objects.create(**domicilio)

# Crear metodos de pago
metodos_pago = [
    {
        'metodo_pago_id': 1,
        'nombre_metodo_pago': 'Tarjeta de Crédito',
        'descripcion': 'Pago con tarjeta de crédito',
    },
    {
        'metodo_pago_id': 2,
        'nombre_metodo_pago': 'PayPal',
        'descripcion': 'Pago con PayPal',
    },
    {
        'metodo_pago_id': 3,
        'nombre_metodo_pago': 'Transferencia Bancaria',
        'descripcion': 'Pago con transferencia bancaria',
    },
    {
        'metodo_pago_id': 4,
        'nombre_metodo_pago': 'Efectivo',
        'descripcion': 'Pago en efectivo',
    },
    {
        'metodo_pago_id': 5,
        'nombre_metodo_pago': 'Cheque',
        'descripcion': 'Pago con cheque',
    },
    {
        'metodo_pago_id': 6,
        'nombre_metodo_pago': 'Bitcoin',
        'descripcion': 'Pago con Bitcoin',
    },
]

for metodo_pago in metodos_pago:
    MetodoPago.objects.create(**metodo_pago)

# Crear usuarios
usuarios = [
    {
        'username':'juanperez',
        'first_name': 'Juan',
        'last_name': 'Pérez',
        'email': 'juan.perez@example.com',
        'password': 'password1',
        'is_staff': True,
        'is_superuser': True
    },
    {
        'username':'mariagonzales',
        'first_name': 'María',
        'last_name': 'González',
        'email': 'maria.gonzalez@example.com',
        'password': 'password2',
        'is_staff': True,
    },
    {
        'username':'davidgarcia',
        'first_name': 'David',
        'last_name': 'García',
        'email': 'david.garcia@example.com',
        'password': 'password5',
        'is_staff': True,
    },
    {
        'username':'carlosrodriguez',
        'first_name': 'Carlos',
        'last_name': 'Rodríguez',
        'email': 'carlos.rodriguez@example.com',
        'password': 'password3',
        'is_staff': False,
    },
    {
        'username':'anamartinez',
        'first_name': 'Ana',
        'last_name': 'Martínez',
        'email': 'ana.martinez@example.com',
        'password': 'password4',
        'is_staff': False,
    },
    {
        'username':'lauralopez',
        'first_name': 'Laura',
        'last_name': 'López',
        'email': 'laura.lopez@example.com',
        'password': 'password6',
        'is_staff': False,
    },
]

for user_data in usuarios:
    user = User(
        username=user_data['username'],
        first_name=user_data['first_name'],
        last_name=user_data['last_name'],
        email=user_data['email'],
        is_staff=user_data.get('is_staff', False),  # Usamos get() en caso de que no esté definido, para dar un valor por defecto
        is_superuser=user_data.get('is_superuser', False)
    )
    user.set_password(user_data['password'])  # Usamos set_password para guardar la contraseña de forma segura
    user.save()

# Crear empleados
empleados = [
    {
        'empleado_id': 1,
        'puesto': 'Gerente',
        'area_trabajo': 'Administración',
        'permisos_acceso': 'Todos',
        'direccion_id': 1,
    },
    {
        'empleado_id': 2,
        'puesto': 'Subgerente',
        'area_trabajo': 'Administración',
        'permisos_acceso': 'Todos',
        'direccion_id': 2,
    },
    {
        'empleado_id': 3,
        'puesto': 'Vendedor',
        'area_trabajo': 'Ventas',
        'permisos_acceso': 'Ventas',
        'direccion_id': 3,
    },
]

for empleado in empleados:
    usuario = User.objects.get(id=empleado['empleado_id'])
    direccion = Domicilio.objects.get(direccion_id=empleado['direccion_id'])
    Empleado.objects.create(
        empleado_id=usuario,
        puesto=empleado['puesto'],
        area_trabajo=empleado['area_trabajo'],
        permisos_acceso=empleado['permisos_acceso'],
        direccion=direccion,
    )

# Crear clientes
clientes = [
    {
        'cliente_id': 4,
        'fecha_registro': '2023-01-01',
        'metodo_pago_predeterminado_id': 1,
        'direccion_predeterminada_id': 1,
    },
    {
        'cliente_id': 5,
        'fecha_registro': '2023-01-15',
        'metodo_pago_predeterminado_id': 2,
        'direccion_predeterminada_id': 2,
    },
    {
        'cliente_id': 6,
        'fecha_registro': '2023-02-01',
        'metodo_pago_predeterminado_id': 3,
        'direccion_predeterminada_id': 3,
    }
]

for cliente in clientes:
    usuario = User.objects.get(id=cliente['cliente_id'])
    metodo_pago = MetodoPago.objects.get(metodo_pago_id=cliente['metodo_pago_predeterminado_id'])
    direccion = Domicilio.objects.get(direccion_id=cliente['direccion_predeterminada_id'])
    Cliente.objects.create(
        cliente_id=usuario,
        fecha_registro=cliente['fecha_registro'],
        metodo_pago_predeterminado=metodo_pago,
        direccion_predeterminada=direccion,
    )

# Crear proveedores
proveedores = [
    {
        'proveedor_id': 1,
        'nombre_empresa': 'Empresa 1',
        'email': 'empresa1@example.com',
        'telefono': '1234567890',
        'direccion_id': 1,
    },
    {
        'proveedor_id': 2,
        'nombre_empresa': 'Empresa 2',
        'email': 'empresa2@example.com',
        'telefono': '0987654321',
        'direccion_id': 2,
    },
    {
        'proveedor_id': 3,
        'nombre_empresa': 'Empresa 3',
        'email': 'empresa3@example.com',
        'telefono': '1122334455',
        'direccion_id': 3,
    },
    {
        'proveedor_id': 4,
        'nombre_empresa': 'Empresa 4',
        'email': 'empresa4@example.com',
        'telefono': '6677889900',
        'direccion_id': 4,
    },
    {
        'proveedor_id': 5,
        'nombre_empresa': 'Empresa 5',
        'email': 'empresa5@example.com',
        'telefono': '2233445566',
        'direccion_id': 5,
    },
    {
        'proveedor_id': 6,
        'nombre_empresa': 'Empresa 6',
        'email': 'empresa6@example.com',
        'telefono': '3344556677',
        'direccion_id': 6,
    },
]

for proveedor in proveedores:
    direccion = Domicilio.objects.get(direccion_id=proveedor['direccion_id'])
    Proveedor.objects.create(
        proveedor_id=proveedor['proveedor_id'],
        nombre_empresa=proveedor['nombre_empresa'],
        email=proveedor['email'],
        telefono=proveedor['telefono'],
        direccion=direccion,
    )

# Crear pedidos de clientes
pedidos_clientes = [
    {
        'pedido_id': 1,
        'cliente_id': 6,
        'fecha_pedido': '2023-04-01',
        'estado_pedido': 'Terminado',
    },
    {
        'pedido_id': 2,
        'cliente_id': 4,
        'fecha_pedido': '2023-04-02',
        'estado_pedido': 'Terminado',
    },
    {
        'pedido_id': 3,
        'cliente_id': 5,
        'fecha_pedido': '2023-04-03',
        'estado_pedido': 'Terminado',
    },
    {
        'pedido_id': 4,
        'cliente_id': 5,
        'fecha_pedido': '2023-04-04',
        'estado_pedido': 'Terminado',
    },
    {
        'pedido_id': 5,
        'cliente_id': 4,
        'fecha_pedido': '2023-04-05',
        'estado_pedido': 'Terminado',
    },
    {
        'pedido_id': 6,
        'cliente_id': 6,
        'fecha_pedido': '2023-04-06',
        'estado_pedido': 'En Proceso',
    },
]

for pedido_cliente in pedidos_clientes:
    cliente = Cliente.objects.get(cliente_id=pedido_cliente['cliente_id'])
    PedidoCliente.objects.create(
        pedido_id=pedido_cliente['pedido_id'],
        cliente=cliente,
        fecha_pedido=pedido_cliente['fecha_pedido'],
        estado_pedido=pedido_cliente['estado_pedido'],
    )

# Crear detalles de pedidos
detalles_pedidos = [
    {
        'detalle_pedido_id': 1,
        'pedido_id': 1,
        'producto_id': 1,
        'cantidad': 2,
    },
    {
        'detalle_pedido_id': 2,
        'pedido_id': 1,
        'producto_id': 2,
        'cantidad': 1,
    },
    {
        'detalle_pedido_id': 3,
        'pedido_id': 2,
        'producto_id': 3,
        'cantidad': 3,
    },
    {
        'detalle_pedido_id': 4,
        'pedido_id': 2,
        'producto_id': 4,
        'cantidad': 1,
    },
    {
        'detalle_pedido_id': 5,
        'pedido_id': 3,
        'producto_id': 5,
        'cantidad': 4,
    },
    {
        'detalle_pedido_id': 6,
        'pedido_id': 3,
        'producto_id': 6,
        'cantidad': 2,
    },
]

for detalle_pedido in detalles_pedidos:
    pedido = PedidoCliente.objects.get(pedido_id=detalle_pedido['pedido_id'])
    producto = Producto.objects.get(producto_id=detalle_pedido['producto_id'])
    DetallePedido.objects.create(
        detalle_pedido_id=detalle_pedido['detalle_pedido_id'],
        pedido=pedido,
        producto=producto,
        cantidad=detalle_pedido['cantidad'],
    )

# Crear facturas
facturas = [
    {
        'factura_id': 1,
        'pedido_id': 1,
        'fecha_emision': '2023-04-01',
        'total': 100.00,
    },
    {
        'factura_id': 2,
        'pedido_id': 2,
        'fecha_emision': '2023-04-02',
        'total': 150.00,
    },
    {
        'factura_id': 3,
        'pedido_id': 3,
        'fecha_emision': '2023-04-03',
        'total': 200.00,
    },
    {
        'factura_id': 4,
        'pedido_id': 4,
        'fecha_emision': '2023-04-04',
        'total': 250.00,
    },
    {
        'factura_id': 5,
        'pedido_id': 5,
        'fecha_emision': '2023-04-05',
        'total': 300.00,
    },
    {
        'factura_id': 6,
        'pedido_id': 6,
        'fecha_emision': '2023-04-06',
        'total': 350.00,
    },
]

for factura in facturas:
    pedido = PedidoCliente.objects.get(pedido_id=factura['pedido_id'])
    Factura.objects.create(
        factura_id=factura['factura_id'],
        pedido=pedido,
        fecha_emision=factura['fecha_emision'],
        total=factura['total'],
    )

# Crear pedidos de proveedores
pedidos_proveedores = [
    {
        'proveedor_id': 1,
        'producto_id': 1,
        'precio_por_unidad': 10.00,
        'fecha_de_compra': '2023-03-01',
        'pedido_entregado': True,
        'pedido_proveedores_ID': 1,
        'pedido_pagado': True,
        'cantidad_comprada': 20,
    },
    {
        'proveedor_id': 2,
        'producto_id': 2,
        'precio_por_unidad': 20.00,
        'fecha_de_compra': '2023-03-02',
        'pedido_entregado': True,
        'pedido_proveedores_ID': 2,
        'pedido_pagado': True,
        'cantidad_comprada': 20,
    },
    {
        'proveedor_id': 3,
        'producto_id': 3,
        'precio_por_unidad': 30.00,
        'fecha_de_compra': '2023-03-03',
        'pedido_entregado': False,
        'pedido_proveedores_ID': 3,
        'pedido_pagado': False,
        'cantidad_comprada': 20,
    },
    {
        'proveedor_id': 4,
        'producto_id': 4,
        'precio_por_unidad': 40.00,
        'fecha_de_compra': '2023-03-04',
        'pedido_entregado': True,
        'pedido_proveedores_ID': 4,
        'pedido_pagado': True,
        'cantidad_comprada': 20,
    },
    {
        'proveedor_id': 5,
        'producto_id': 5,
        'precio_por_unidad': 50.00,
        'fecha_de_compra': '2023-03-05',
        'pedido_entregado': False,
        'pedido_proveedores_ID': 5,
        'pedido_pagado': False,
        'cantidad_comprada': 20,
    },
    {
        'proveedor_id': 6,
        'producto_id': 6,
        'precio_por_unidad': 60.00,
        'fecha_de_compra': '2023-03-06',
        'pedido_entregado': True,
        'pedido_proveedores_ID': 6,
        'pedido_pagado': True,
        'cantidad_comprada': 20,
    },
]

for pedido_proveedor in pedidos_proveedores:
    proveedor = Proveedor.objects.get(proveedor_id=pedido_proveedor['proveedor_id'])
    producto = Producto.objects.get(producto_id=pedido_proveedor['producto_id'])
    PedidoProveedor.objects.create(
        proveedor=proveedor,
        producto=producto,
        precio_por_unidad=pedido_proveedor['precio_por_unidad'],
        fecha_de_compra=pedido_proveedor['fecha_de_compra'],
        pedido_entregado=pedido_proveedor['pedido_entregado'],
        pedido_proveedores_ID=pedido_proveedor['pedido_proveedores_ID'],
        pedido_pagado=pedido_proveedor['pedido_pagado'],
        cantidad_comprada=pedido_proveedor['cantidad_comprada'],
    )