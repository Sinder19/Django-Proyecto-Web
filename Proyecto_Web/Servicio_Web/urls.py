from django.urls import path
from .views import ver_productos, agregar_producto, modificar_producto, eliminar_producto
from .viewslogin import login

urlpatterns = [
    path('ver_productos', ver_productos, name="ver_productos"),
    path('agregar_producto', agregar_producto,name="agregar_producto"),
    path('modificar_producto/<id>', modificar_producto, name="modificar_producto"),
    path('eliminar_producto/<id>', eliminar_producto, name="eliminar_producto"),
    path('login', login, name="login"),
]