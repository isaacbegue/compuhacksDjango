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
    path('perfil_rh/', views.provisional, name='perfil_rh'),
    path('perfil_rh/<str:nombreprovisional>/', views.provisional, name='perfil_rh'),
    path('reportes_internos/', views.reportes_internos, name='reportes_internos'),
    path('reportes_internos/<str:nombreprovisional>/', views.reportes_internos, name='reportes_internos'),

#usuario externo
    path('pedidos/', views.provisional, name='pedidos'),
    path('pedidos/<str:nombreprovisional>/', views.provisional, name='pedidos'),
    path('configuracion_cuenta/', views.provisional, name='configuracion_cuenta'),
    path('configuracion_cuenta/<str:nombreprovisional>/', views.provisional, name='configuracion_cuenta'),
    path('metodos_pago/', views.provisional, name='metodos_pago'),
    path('metodos_pago/<str:nombreprovisional>/', views.provisional, name='metodos_pago'),
    path('lista_deseados/', views.provisional, name='lista_deseados'),
    path('lista_deseados/<str:nombreprovisional>/', views.provisional, name='lista_deseados'),

]
