
from django.shortcuts import render, get_object_or_404 , redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Producto, User
from django.contrib.auth import logout
from django.shortcuts import redirect

def cerrar_sesion(request):
    logout(request)
    # Redirige al usuario a la página principal (o cualquier otra página) después de cerrar la sesión.
    return redirect('index')

# Create your views here.

def index(request):
    return render(request, 'tienda/index.html')

def detalle_producto(request):
    return render(request, 'tienda/detalle_producto.html')

def carrito_compras(request):

    return render(request, 'tienda/carrito_compras.html')


def ingresar(request):
    if request.method == "POST":
        usuario = request.POST['usuario']
        password = request.POST['password']
        user = authenticate(request, username=usuario, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Has ingresado exitosamente.')
            # Redirige al usuario a la página que desees tras una autenticación exitosa
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'tienda/ingresar.html')

def registrarse(request):
    return render(request, 'tienda/registrarse.html')

def provisional(request, nombreprovisional="Página provisional"):
    return render(request, 'tienda/provisional.html',{'nombreprovisional' : nombreprovisional})


# Perfil de usuario desglose

def perfil_usuario(request):
    return render(request, 'tienda/perfil_usuario.html')

def perfil_rh(request):
    return render(request, 'tienda/perfil_usuario/perfil_rh.html')

def reportes_internos(request):
    return render(request, 'tienda/dashboard/dashboard/index.html')

def contabilidad(request):
    return render(request, 'tienda/perfil_usuario/contabilidad.html')

def almacen(request):
    return render(request, 'tienda/perfil_usuario/almacen.html')

def recursos_humanos(request):
    return render(request, 'tienda/perfil_usuario/recursos_humanos.html')

def mercadotecnia(request):
    return render(request, 'tienda/perfil_usuario/mercadotecnia.html')

def pedidos(request):
    return render(request, 'tienda/perfil_usuario/pedidos.html')

def configuracion_cuenta(request):
    return render(request, 'tienda/perfil_usuario/configuracion_cuenta.html')

def metodos_pago(request):
    return render(request, 'tienda/perfil_usuario/metodos_pago.html')

def lista_deseados(request):
    return render(request, 'tienda/perfil_usuario/lista_deseados.html')

def balance_cuentas(request):
    return render(request, 'tienda/perfil_usuario/contabilidad/balance_cuentas.html')

def kpis_contabilidad(request):
    return render(request, 'tienda/perfil_usuario/contabilidad/kpis_contables.html')

def envios_pendientes(request):
    return render(request, 'tienda/perfil_usuario/almacen/envios_pendientes.html')

def kpis_almacen(request):
    return render(request, 'tienda/perfil_usuario/almacen/kpis_almacen.html')

