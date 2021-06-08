from django.contrib import admin
from django.urls import path, include
from .views import Home, Quienes_somos, Polerones, Poleras, Pantalones, Contactanos_mensaje, Registrarse, Ingresar_usuario, Inicio_sesion, Olvidaste_clave, Detalle_producto, Carrito, Buscar_polerones, Buscar_poleras, Buscar_pantalones, Enviar_contactanos, Administrar_prod, Administrar_usu, Eliminar_prod, Modificar_prod, Modificar

urlpatterns = [
    path('', Home, name="Home"),
    path('Quienes_somos', Quienes_somos, name="Quienes_somos"),
    path('Polerones', Polerones, name="Polerones"),
    path('Poleras', Poleras, name="Poleras"),
    path('Pantalones', Pantalones, name="Pantalones"),
    path('Contactanos_mensaje', Contactanos_mensaje, name="Contactanos_mensaje"),
    path('Enviar_contactanos', Enviar_contactanos, name="Enviar_contactanos"),
    path('Registrarse', Registrarse, name="Registrarse"),
    path('Ingresar_usuario', Ingresar_usuario, name="Ingresar_usuario"),
    path('Inicio_sesion', Inicio_sesion, name="Inicio_sesion"),
    path('Olvidaste_clave', Olvidaste_clave, name="Olvidaste_clave"),
    path('Detalle_producto', Detalle_producto, name="Detalle_producto"),
    path('Carrito', Carrito, name="Carrito"),
    path('Buscar_polerones', Buscar_polerones, name="Buscar_polerones"),
    path('Buscar_poleras', Buscar_poleras, name="Buscar_poleras"),
    path('Buscar_pantalones', Buscar_pantalones, name="Buscar_pantalones"),
    path('Administrar_prod', Administrar_prod, name="Administrar_prod"),
    path('Eliminar_prod/<int:id>', Eliminar_prod, name="Eliminar_prod"),
    path('Modificar_prod/<int:id>', Modificar_prod, name="Modificar_prod"),
    path('Modificar', Modificar, name="Modificar"),
    path('Administrar_usu', Administrar_usu, name="Administrar_usu"),
]
