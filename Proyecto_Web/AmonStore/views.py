from typing import ContextManager
from django.contrib import messages
from django.db import models
from django.shortcuts import render, redirect
from .models import Direccion, Producto, Comuna, Region, TipoProducto, TipoUsuario, Usuario, Contactanos, Carrito

# Create your views here.
def Home(request):
    return render(request, 'AmonStore/Home.html')

def Quienes_somos(request):
    return render(request, 'AmonStore/Quienes_somos.html')

def Polerones(request):
    polerones = Producto.objects.filter(tipoproducto = 1)
    contexto = {"producto": polerones}
    return render(request, 'AmonStore/Productos/polerones.html', contexto)

def Buscar_polerones(request):
    buscar = request.POST['buscar']
    polerones = Producto.objects.filter(tipoproducto = 1, nombreProd__icontains = buscar)
    contexto = {"producto": polerones}
    return render(request, 'AmonStore/Productos/polerones.html', contexto)

def Poleras(request):
    poleras = Producto.objects.filter(tipoproducto = 2)
    contexto = {"producto": poleras}
    return render(request, 'AmonStore/Productos/poleras.html', contexto)

def Buscar_poleras(request):
    buscar = request.POST['buscar']
    polerones = Producto.objects.filter(tipoproducto = 2, nombreProd__icontains = buscar)
    contexto = {"producto": polerones}
    return render(request, 'AmonStore/Productos/poleras.html', contexto)

def Pantalones(request):
    pantalones = Producto.objects.filter(tipoproducto = 3)
    contexto = {"producto": pantalones}
    return render(request, 'AmonStore/Productos/Pantalones.html', contexto)

def Buscar_pantalones(request):
    buscar = request.POST['buscar']
    polerones = Producto.objects.filter(tipoproducto = 3, nombreProd__icontains = buscar)
    contexto = {"producto": polerones}
    return render(request, 'AmonStore/Productos/Pantalones.html', contexto) 

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

def Carrito(request):
    return render(request, 'AmonStore/carrito.html')

def Administrar_prod(request):
    productos = Producto.objects.order_by('idProducto')
    contexto = {"producto": productos}
    return render(request, 'AmonStore/Administracion/Administrar_productos.html', contexto)

def Eliminar_prod(request, id):
    producto = Producto.objects.get(idProducto = id)
    producto.delete() #elimina el registro
    messages.success(request,'Producto Eliminado')

    return redirect('Administrar_prod')

def Modificar_prod(request, id):
    producto = Producto.objects.get(idProducto = id)
    tipo_prod = TipoProducto.objects.all()
    contexto = {
        "producto": producto,
        "tipo_prod": tipo_prod,    
    }

    return render (request, 'AmonStore/Administracion/Modificar_prod.html', contexto)

def Modificar(request):
    id = request.POST['id']
    nombre = request.POST['nombre']
    precio = request.POST['precio']
    descripcion = request.POST['descripcion']
    stock = request.POST['stock']
    tipo_prod = request.POST['tipo_prod']
    talla = request.POST['talla']
    color = request.POST['color']

    producto = Producto.objects.get(idProducto = id)
    
    if producto.nombreProd != nombre:
        producto.nombreProd = nombre

    if producto.precioProd != precio:
        producto.precioProd = precio

    if producto.descripcionProd != descripcion:
        producto.descripcionProd = descripcion

    if producto.stockProd != stock:
        producto.stockProd = stock

    if producto.tallaProd != talla:
        producto.tallaProd = talla

    if producto.colorProd != color:
        producto.colorProd = color
    
    tipo_prod2 = TipoProducto.objects.get(idTipoProd = tipo_prod)
    if producto.tipoproducto != tipo_prod2:
        producto.tipoproducto = tipo_prod2
    
    producto.save()
    messages.success(request, 'Producto Modificado')
    return redirect('Administrar_prod')

def Agregar_prod(request):
    tipo_prod = TipoProducto.objects.all()
    contexto = {
        "tipo_prod" : tipo_prod
    }
    return render(request, 'AmonStore/Administracion/Agregar_prod.html', contexto)

def Agregar_producto(request):
    nombre = request.POST['nombre']
    precio = request.POST['precio']
    descripcion = request.POST['descripcion']
    foto = request.FILES['foto']
    stock = request.POST['stock']
    tipoprod = request.POST['tipoproducto']
    talla = request.POST['talla']
    color = request.POST['color']

    tipoproducto2 = TipoProducto.objects.get(idTipoProd = tipoprod)

    Producto.objects.create(nombreProd = nombre, precioProd = precio, descripcionProd = descripcion, fotoProd = foto, stockProd = stock, tipoproducto = tipoproducto2, tallaProd = talla, colorProd = color)

    messages.success(request, 'El Producto Ha Sido Agregado Con Exito')
    return redirect('Administrar_prod') 

def Administrar_usu(request):
    usuarios = Usuario.objects.order_by('rutUsu')
    contexto = {"usuarios": usuarios}

    return render(request, 'AmonStore/Administracion/Administrar_usuarios.html', contexto)

def Eliminar_usu(request, rut):
    usuarios = Usuario.objects.get(rutUsu = rut)
    usuarios.delete() #elimina el registro
    messages.success(request,'Usuario Eliminado con Exito')

    return redirect('Administrar_usu')

def Modificar_usu(request, rut):
    usuarios = Usuario.objects.get(rutUsu = rut)
    tipo_usu = TipoUsuario.objects.all()
    contexto = {
        "usuarios": usuarios,
        "tipo_usu": tipo_usu,    
    }

    return render (request, 'AmonStore/Administracion/Modificar_usu.html', contexto)

def Modificar_usuario(request):
    rutUsu = request.POST['rutUsu']
    nombreUsu = request.POST['nombreUsu']
    apellidoUsu = request.POST['apellidoUsu']
    correoUsu = request.POST['correoUsu']
    contrasenaUsu = request.POST['contrasenaUsu1']
    telefonoUsu = request.POST['telefonoUsu']
    tipousuario = request.POST['tipousuario']

    usuario = Usuario.objects.get(rutUsu = rutUsu)

    if usuario.nombreUsu != nombreUsu:
        usuario.nombreUsu = nombreUsu

    if usuario.apellidoUsu != apellidoUsu:
        usuario.apellidoUsu = apellidoUsu

    if usuario.correoUsu != correoUsu:
        usuario.correoUsu = correoUsu

    if usuario.contrasenaUsu != contrasenaUsu:
        usuario.contrasenaUsu = contrasenaUsu
        
    if usuario.telefonoUsu != telefonoUsu:
        usuario.telefonoUsu = telefonoUsu
    
    tipousuario2 = TipoUsuario.objects.get(idTipoUsu = tipousuario)
    if usuario.tipousuario != tipousuario2:
        usuario.tipousuario = tipousuario2
    
    usuario.save()
    messages.success(request, 'Usuario Modificado')
    return redirect('Administrar_usu')
    
def Ver_poleron(request, id):
    producto = Producto.objects.get(idProducto = id)
    contexto = {"producto":producto}

    return render(request, 'AmonStore/Productos/detalle_poleron.html', contexto)

def Ver_polera(request, id):
    producto = Producto.objects.get(idProducto = id)
    contexto = {"producto":producto}

    return render(request, 'AmonStore/Productos/detalle_polera.html', contexto)

def Ver_pantalon(request, id):
    producto = Producto.objects.get(idProducto = id)
    contexto = {"producto":producto}

    return render(request, 'AmonStore/Productos/detalle_pantalon.html', contexto)


def Carrito_poleron(request, id):
    cant = request.POST['cantidad']
    
    poleron = Producto.objects.get(idProducto = id)
    usuario = Usuario.objects.get(rutUsu = '20832119-6')

    Carrito.objects.create(producto = poleron, cantidadProd = cant, usuario = usuario)

    messages.success(request, 'El Producto Ha Sido Agregado al Carrito')
    return redirect('Ver_poleron')
