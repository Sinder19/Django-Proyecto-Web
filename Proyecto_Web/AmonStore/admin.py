from django.contrib import admin
from .models import Region, Comuna, TipoUsuario, Usuario, Direccion, Venta, TipoProducto, Producto, DetalleVenta, Contactanos, Carrito, MensajeVisto
 
# Register your models here.
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(TipoUsuario)
admin.site.register(Usuario)
admin.site.register(Direccion)
admin.site.register(Venta)
admin.site.register(TipoProducto)
admin.site.register(Producto)
admin.site.register(DetalleVenta)
admin.site.register(Contactanos)
admin.site.register(Carrito)
admin.site.register(MensajeVisto)