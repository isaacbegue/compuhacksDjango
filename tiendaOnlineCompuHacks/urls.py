from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    
    path('carrito_compras', views.carrito_compras, name='carrito_compras'),
    path('ingresar', views.ingresar, name='ingresar'),
    path('registrarse', views.registrarse, name='registrarse'),
    path('cerrar_sesion', views.cerrar_sesion, name='cerrar_sesion'),
    path('perfil_usuario', views.perfil_usuario, name='perfil_usuario'),
    
#usuario autenticado
    path('provisional/', views.provisional, name='provisional_default'),
    path('provisional/<str:nombreprovisional>/', views.provisional, name='provisional'),
    
#usuario interno    
    path('perfil_rh/', views.perfil_rh, name='perfil_rh'),
    path('perfil_rh/<str:nombreprovisional>/', views.perfil_rh, name='perfil_rh'),
    path('reportes_internos/', views.reportes_internos, name='reportes_internos'),
    path('reportes_internos/<str:nombreprovisional>/', views.reportes_internos, name='reportes_internos'),
    path('contabilidad/', views.contabilidad, name='contabilidad'),
    path('contabilidad/<str:nombreprovisional>/', views.contabilidad, name='contabilidad'),
    path('almacen/', views.almacen, name='almacen'),
    path('almacen/<str:nombreprovisional>/', views.almacen, name='almacen'),
    path('recursos_humanos/', views.recursos_humanos, name='recursos_humanos'),
    path('recursos_humanos/<str:nombreprovisional>/', views.recursos_humanos, name='recursos_humanos'),
    path('mercadotecnia/', views.mercadotecnia, name='mercadotecnia'),
    path('mercadotecnia/<str:nombreprovisional>/', views.mercadotecnia, name='mercadotecnia'),

    path('almacen/envios_pendientes', views.envios_pendientes, name='almacen/envios_pendientes'),
    path('almacen/kpis_almacen', views.kpis_almacen, name='almacen/kpis_almacen'),

    path('contabilidad/balance_cuentas', views.balance_cuentas, name='contabilidad/balance_cuentas'),
    path('contabilidad/kpis_contabilidad', views.kpis_contabilidad, name='contabilidad/kpis_contabilidad'),

#usuario externo
    path('pedidos/', views.pedidos, name='pedidos'),
    path('pedidos/<str:nombreprovisional>/', views.pedidos, name='pedidos'),
    path('configuracion_cuenta/', views.configuracion_cuenta, name='configuracion_cuenta'),
    path('configuracion_cuenta/<str:nombreprovisional>/', views.configuracion_cuenta, name='configuracion_cuenta'),
    path('metodos_pago/', views.metodos_pago, name='metodos_pago'),
    path('metodos_pago/<str:nombreprovisional>/', views.metodos_pago, name='metodos_pago'),
    path('lista_deseados/', views.lista_deseados, name='lista_deseados'),
    path('lista_deseados/<str:nombreprovisional>/', views.lista_deseados, name='lista_deseados'),
]
