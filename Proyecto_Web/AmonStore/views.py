from typing import ContextManager
from django.contrib import messages
from django.db import models
from django.shortcuts import render, redirect
from .models import Direccion, Producto, Comuna, Region, TipoUsuario, Usuario, Contactanos

# Create your views here.
def Home(request):
    return render(request, 'AmonStore/Home.html')

def Quienes_somos(request):
    return render(request, 'AmonStore/Quienes_somos.html')

def Polerones(request):
    polerones = Producto.objects.filter(tipoproducto = 1)
    contexto = {"producto": polerones}
    return render(request, 'AmonStore/polerones.html', contexto)

def Buscar_polerones(request):
    buscar = request.POST['buscar']
    polerones = Producto.objects.filter(tipoproducto = 1, nombreProd__icontains = buscar)
    contexto = {"producto": polerones}
    return render(request, 'AmonStore/polerones.html', contexto)

def Poleras(request):
    poleras = Producto.objects.filter(tipoproducto = 2)
    contexto = {"producto": poleras}
    return render(request, 'AmonStore/poleras.html', contexto)

def Buscar_poleras(request):
    buscar = request.POST['buscar']
    polerones = Producto.objects.filter(tipoproducto = 2, nombreProd__icontains = buscar)
    contexto = {"producto": polerones}
    return render(request, 'AmonStore/poleras.html', contexto)

def Pantalones(request):
    pantalones = Producto.objects.filter(tipoproducto = 3)
    contexto = {"producto": pantalones}
    return render(request, 'AmonStore/Pantalones.html', contexto)

def Buscar_pantalones(request):
    buscar = request.POST['buscar']
    polerones = Producto.objects.filter(tipoproducto = 3, nombreProd__icontains = buscar)
    contexto = {"producto": polerones}
    return render(request, 'AmonStore/Pantalones.html', contexto) 

def Contactanos_mensaje(request):
    return render(request, 'AmonStore/contactanos.html')

def Enviar_contactanos(request):
    nombre = request.POST['nombre_completo']
    correo = request.POST['correo']
    asunto = request.POST['asunto']
    comentario = request.POST['comentario']

    Contactanos.objects.create(nombre = nombre, correo = correo, asunto = asunto, comentario = comentario, visto = 2)
    messages.success(request, 'El mensaje ha sido enviado con exito')
    return redirect('Contactanos_mensaje')

def Registrarse(request):
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    contexto = {
        "region" : regiones, 
        "comuna" : comunas
    }
    return render(request, 'AmonStore/Registrarse.html', contexto)

def Ingresar_usuario(request):
    rut = request.POST['rut']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    correo = request.POST['email']
    contrasenia = request.POST['contrasenia2']
    telefono = request.POST['telefono']
    comunaUsu = request.POST['comunas']
    direccion = request.POST['direccion']
    num_direc = request.POST['direccion_num']
    block = request.POST['block']
    num_dpto = request.POST['num_depto']
    desp_dic = request.POST['desp_dic']
 
    com = Comuna.objects.get(idComuna = comunaUsu)
    tipoUsu = TipoUsuario.objects.get(idTipoUsu = 2)
    
    if (desp_dic == 'si'):
        opcionDespacho = 1
    elif (desp_dic == 'no'):
        opcionDespacho = 2
    
    Usuario.objects.create(rutUsu = rut, nombreUsu = nombre, apellidoUsu = apellido, correoUsu = correo, contrasenaUsu = contrasenia, telefonoUsu = telefono, tipousuario = tipoUsu)
    
    usu = Usuario.objects.get(rutUsu = rut)
    Direccion.objects.create(descripcion = direccion, numDic =num_direc, blockDpto = block, numDpto = num_dpto, direccionDespacho = opcionDespacho, comuna = com, usuario = usu)

    messages.success(request, 'El Usuario Ha Sido Registrado Con Exito')
    return redirect('Registrarse')

def Inicio_sesion(request):
    return render(request, 'AmonStore/inicio_sesion.html')

def Olvidaste_clave(request):
    return render(request, 'AmonStore/olvidaste_clave.html')

def Detalle_producto(request):
    return render(request, 'AmonStore/detalle_producto.html')

def Carrito(request):
    return render(request, 'AmonStore/carrito.html')