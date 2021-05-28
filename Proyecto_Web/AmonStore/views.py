from django.shortcuts import render, resolve_url

# Create your views here.
def Home(request):
    return render(request, 'AmonStore/Home.html')

def Quienes_somos(request):
    return render(request, 'AmonStore/Quienes_somos.html')

def Polerones(request):
    return render(request, 'AmonStore/polerones.html')

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