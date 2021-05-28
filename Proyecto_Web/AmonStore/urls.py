from django.contrib import admin
from django.urls import path, include
from .views import Home, Quienes_somos, Polerones, Poleras, Pantalones, Contactanos, Registrarse, Inicio_sesion, Olvidaste_clave, Detalle_producto, Carrito

urlpatterns = [
    path('', Home, name="Home"),
    path('Quienes_somos', Quienes_somos, name="Quienes_somos"),
    path('Polerones', Polerones, name="Polerones"),
    path('Poleras', Poleras, name="Poleras"),
    path('Pantalones', Pantalones, name="Pantalones"),
    path('Contactanos', Contactanos, name="Contactanos"),
    path('Registrarse', Registrarse, name="Registrarse"),
    path('Inicio_sesion', Inicio_sesion, name="Inicio_sesion"),
    path('Olvidaste_clave', Olvidaste_clave, name="Olvidaste_clave"),
    path('Detalle_producto', Detalle_producto, name="Detalle_producto"),
    path('Carrito', Carrito, name="Carrito"),
]
