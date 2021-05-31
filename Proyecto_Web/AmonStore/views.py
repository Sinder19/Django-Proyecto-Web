from typing import ContextManager
from django.db import models
from django.shortcuts import render, resolve_url
from .models import Producto, TipoProducto

# Create your views here.
def Home(request):
    return render(request, 'AmonStore/Home.html')

def Quienes_somos(request):
    return render(request, 'AmonStore/Quienes_somos.html')

def Polerones(request):
    polerones = Producto.objects.filter(tipoproducto = 2)
    contexto = {"producto":polerones}
    return render(request, 'AmonStore/polerones.html', contexto)

def Poleras(request):
    return render(request, 'AmonStore/poleras.html')

def Pantalones(request):
    return render(request, 'AmonStore/Pantalones.html')

def Contactanos(request):
    return render(request, 'AmonStore/contactanos.html')

def Registrarse(request):
    return render(request, 'AmonStore/Registrarse.html')

def Inicio_sesion(request):
    return render(request, 'AmonStore/inicio_sesion.html')

def Olvidaste_clave(request):
    return render(request, 'AmonStore/olvidaste_clave.html')

def Detalle_producto(request):
    return render(request, 'AmonStore/detalle_producto.html')

def Carrito(request):
    return render(request, 'AmonStore/carrito.html')