from django.contrib import messages
from django.db.models import Sum, Count
from django.shortcuts import render, redirect
from .models import Direccion, Producto, Comuna, Region, TipoProducto, TipoUsuario, Usuario, Contactanos, Carrito, MensajeVisto
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 

from django.contrib.auth.hashers import make_password

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
    
    mensajevisto2 = MensajeVisto.objects.get(idTipo = 2)

    Contactanos.objects.create(nombre = nombre, correo = correo, asunto = asunto, comentario = comentario, mensajevisto = mensajevisto2)
    messages.success(request, 'El mensaje ha sido enviado con exito')
    return redirect('Contactanos_mensaje')

def Administrar_men(request):
    mensaje = Contactanos.objects.order_by('idContac')
    contexto ={
        "mensaje":mensaje,
    }
    return render(request, 'AmonStore/Administracion/Administrar_mensajes.html', contexto)

def Modificar_men(request, id):
    mensaje = Contactanos.objects.get(idContac = id)
    tipo = MensajeVisto.objects.all()

    contexto ={
        "mensaje":mensaje,
        "tipo":tipo
    }
    return render(request, 'AmonStore/Administracion/Modificar_men.html', contexto)

def Modificar_mensaje(request):
    tipo = request.POST['tipo_men']
    id_men = request.POST['id_men']

    mensaje = Contactanos.objects.get(idContac = id_men)
    tipo2 = MensajeVisto.objects.get(idTipo = tipo)

    mensaje.mensajevisto = tipo2
    mensaje.save()
    
    messages.success(request, 'Mensaje Modificado')
    return redirect('Administrar_men')

def Eliminar_men(request, id):
    mensaje = Contactanos.objects.get(idContac = id)
    mensaje.delete()
    messages.success(request, 'El Mensaje Ha Sido Eliminado')
    return redirect('Administrar_men')

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
    User.objects.create_user(id = int(rut), username = correo, password = contrasenia, first_name = nombre, last_name = apellido, email = correo, is_staff = 1, is_superuser = 0)

    usu = Usuario.objects.get(rutUsu = rut)
    Direccion.objects.create(descripcion = direccion, numDic =num_direc, blockDpto = block, numDpto = num_dpto, direccionDespacho = opcionDespacho, comuna = com, usuario = usu)

    messages.success(request, 'El Usuario Ha Sido Registrado Con Exito')
    return redirect('Registrarse')

def Inicio_sesion(request):
    return render(request, 'AmonStore/inicio_sesion.html')

def Olvidaste_clave(request):
    return render(request, 'AmonStore/olvidaste_clave.html')    


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
    foto = request.FILES['foto']

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
    
    if foto is not None:
        producto.fotoProd = foto

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
    usu = User.objects.get(id = rut)
    usuarios.delete() #elimina el registro
    usu.delete()
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
    telefonoUsu = request.POST['telefonoUsu']
    tipousuario = request.POST['tipousuario']

    usuario = Usuario.objects.get(rutUsu = rutUsu)
    usu = User.objects.get(id = int(rutUsu))

    if usuario.nombreUsu != nombreUsu:
        usuario.nombreUsu = nombreUsu
        usu.first_name = nombreUsu

    if usuario.apellidoUsu != apellidoUsu:
        usuario.apellidoUsu = apellidoUsu
        usu.last_name = apellidoUsu

    if usuario.correoUsu != correoUsu:
        usuario.correoUsu = correoUsu
        usu.email = correoUsu

    if usuario.telefonoUsu != telefonoUsu:
        usuario.telefonoUsu = telefonoUsu
    
    tipousuario2 = TipoUsuario.objects.get(idTipoUsu = tipousuario)
    if tipousuario2.idTipoUsu == 1:
        usu.is_superuser = 1
    if tipousuario2.idTipoUsu == 2:
        usu.is_superuser = 0
    if usuario.tipousuario != tipousuario2:
        usuario.tipousuario = tipousuario2
    
    usuario.save()
    usu.save()
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
    usuario = Usuario.objects.get(rutUsu = request.user.id)

    total = int(cant) * int(poleron.precioProd)

    Carrito.objects.create(cantidadProd = cant, totalProd = total, usuario = usuario, producto = poleron)
    messages.success(request, 'El Producto Ha Sido Agregado al ')
    return redirect('Polerones')

def Carrito_polera(request, id):
    cant = request.POST['cantidad']
    
    polera = Producto.objects.get(idProducto = id)
    usuario = Usuario.objects.get(rutUsu = request.user.id)

    total = int(cant) * int(polera.precioProd)

    Carrito.objects.create(producto = polera, cantidadProd = cant, totalProd = total, usuario = usuario)

    messages.success(request, 'El Producto Ha Sido Agregado al ')
    return redirect('Poleras')

def Carrito_pantalon(request, id):
    cant = request.POST['cantidad']
    
    pantalon = Producto.objects.get(idProducto = id)
    usuario = Usuario.objects.get(rutUsu = request.user.id)

    total = int(cant) * int(pantalon.precioProd)

    Carrito.objects.create(producto = pantalon, cantidadProd = cant, totalProd = total, usuario = usuario)

    messages.success(request, 'El Producto Ha Sido Agregado al ')
    return redirect('Pantalones')

def Ver_carrito(request):
    usuario2 = Usuario.objects.get(rutUsu = request.user.id)
    carrito = Carrito.objects.filter(usuario = usuario2)
    
    suma2 = Carrito.objects.filter(usuario = usuario2).count()
    
    if suma2 == 0:
        suma = 0
        x = 0
    else:
        suma = Carrito.objects.filter(usuario = usuario2).aggregate(Sum('totalProd'))
        x = 1

    contexto = {
        "carrito":carrito,
        "suma":suma,
        "x": x,
    }

    return render(request, 'AmonStore/carrito.html', contexto)

def Eliminar_prod_carrito(request, id):
    carrito = Carrito.objects.get(idCarrito = id)
    carrito.delete() #elimina el registro
    messages.success(request,'Producto Eliminado Exitosamente')

    return redirect('Ver_carrito')

def login_view(request):
    u = request.POST['username']
    c = request.POST['password']

    user = authenticate(username = u, password = c)

    if user is not None:
        if user.is_active:
            login(request,user)
            return redirect('Home')
        else:
            messages.error(request,'Usuario Inactivo')
    else:
        messages.error(request,'Usuario y/o contraseña incorrecta')

    return redirect('InicioSesion')

def logout_view(request):

    logout(request)
    return redirect('Home')

def Mi_perfil(request):
    usuario = Usuario.objects.get(rutUsu = request.user.id)
    contexto = {
        "usuario": usuario
    }
    return render(request, 'AmonStore/Mi_perfil.html', contexto)

def Modificar_usuario_Miperfil(request):
    rutUsu = request.POST['rutUsu']
    nombreUsu = request.POST['nombreUsu']
    apellidoUsu = request.POST['apellidoUsu']
    correoUsu = request.POST['correoUsu']
    contrasenaUsu = request.POST['contrasenaUsu1']
    telefonoUsu = request.POST['telefonoUsu']

    usuario = Usuario.objects.get(rutUsu = rutUsu)
    usu = User.objects.get(id = int(rutUsu))

    if usuario.nombreUsu != nombreUsu:
        usuario.nombreUsu = nombreUsu
        usu.first_name = nombreUsu

    if usuario.apellidoUsu != apellidoUsu:
        usuario.apellidoUsu = apellidoUsu
        usu.last_name = apellidoUsu

    if usuario.correoUsu != correoUsu:
        usuario.correoUsu = correoUsu
        usu.email = correoUsu
    
    if usuario.telefonoUsu != telefonoUsu:
        usuario.telefonoUsu = telefonoUsu

    mensaje = 'Usuario Modificado'

    if usuario.contrasenaUsu != contrasenaUsu:
        usuario.contrasenaUsu = contrasenaUsu
        usu.password = make_password(contrasenaUsu)
        mensaje = mensaje + ', Por favor vuelve a iniciar sesion con tu nueva contraseña'
        
        
    usuario.save()
    usu.save()
    messages.success(request, mensaje)
    return redirect('Mi_perfil')
