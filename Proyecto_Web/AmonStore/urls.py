from django.contrib import admin
from django.urls import path
from .views import Home, Quienes_somos, Polerones, Poleras, Pantalones, Contactanos_mensaje, Registrarse, Ingresar_usuario, Inicio_sesion, Olvidaste_clave, Buscar_polerones, Buscar_poleras, Buscar_pantalones, Enviar_contactanos, Administrar_prod, Administrar_usu, Eliminar_prod, Modificar_prod, Modificar, Eliminar_usu, Modificar_usu, Modificar_usuario, Agregar_prod, Agregar_producto, Ver_poleron, Ver_polera, Ver_pantalon, Carrito_poleron, Carrito_polera, Carrito_pantalon, Ver_carrito, Eliminar_prod_carrito, login_view, logout_view, Mi_perfil, Modificar_usuario_Miperfil
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

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
    path('Buscar_polerones', Buscar_polerones, name="Buscar_polerones"),
    path('Buscar_poleras', Buscar_poleras, name="Buscar_poleras"),
    path('Buscar_pantalones', Buscar_pantalones, name="Buscar_pantalones"),
    path('Administrar_prod', login_required(Administrar_prod), name="Administrar_prod"),
    path('Eliminar_prod/<int:id>', login_required(Eliminar_prod), name="Eliminar_prod"),
    path('Modificar_prod/<int:id>', login_required(Modificar_prod), name="Modificar_prod"),
    path('Modificar', login_required(Modificar), name="Modificar"),
    path('Administrar_usu', login_required(Administrar_usu), name="Administrar_usu"),
    path('Eliminar_usu/<rut>', login_required(Eliminar_usu), name="Eliminar_usu"),
    path('Modificar_usu/<rut>', login_required(Modificar_usu), name="Modificar_usu"),
    path('Modificar_usuario', login_required(Modificar_usuario), name="Modificar_usuario"),
    path('Agregar_prod', login_required(Agregar_prod), name="Agregar_prod"),
    path('Agregar_producto', login_required(Agregar_producto), name="Agregar_producto"),
    path('Ver_poleron/<int:id>', Ver_poleron, name="Ver_poleron"),
    path('Ver_polera/<int:id>', Ver_polera, name="Ver_polera"),
    path('Ver_pantalon/<int:id>', Ver_pantalon, name="Ver_pantalon"),
    path('Carrito_poleron/<int:id>', login_required(Carrito_poleron), name="Carrito_poleron"),
    path('Carrito_polera/<int:id>', login_required(Carrito_polera), name="Carrito_polera"),
    path('Carrito_pantalon/<int:id>', login_required(Carrito_pantalon), name="Carrito_pantalon"),
    path('Carrito', login_required(Ver_carrito), name="Ver_carrito"),
    path('Eliminar_prod_carrito/<int:id>', login_required(Eliminar_prod_carrito), name="Eliminar_prod_carrito"),
    path('Mi_perfil', login_required(Mi_perfil), name="Mi_perfil"),
    path('Modificar_MiPerfil', Modificar_usuario_Miperfil, name="Modificar_usuario_Miperfil"),

    path('InicioSesion/', LoginView.as_view(template_name='AmonStore/inicio_sesion.html'), name="InicioSesion"),
    path('Sesion', login_view, name="Sesion"),
    path('logout', logout_view, name="logout"),
]
