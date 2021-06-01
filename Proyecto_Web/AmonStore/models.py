from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.
class Region(models.Model):
    idRegion = models.AutoField(primary_key=True, verbose_name="Id de la Región")
    nombreRegion = models.CharField(max_length=30, verbose_name="Nombre de la Región", blank=False, null=False)

    def __str__(self) -> str:
        return self.nombreRegion

class Comuna(models.Model):
    idComuna = models.AutoField(primary_key=True, verbose_name="Id de la Comuna")
    nombreComuna = models.CharField(max_length=30, verbose_name="Nombre de la Comuna", blank=False, null=False)
    region = models.ForeignKey(Region, on_delete=CASCADE)

    def __str__(self) -> str:
        return self.nombreComuna

class TipoUsuario(models.Model):
    idTipoUsu = models.AutoField(primary_key=True, verbose_name="Id del Tipo de Usuario")
    descripcion = models.CharField(max_length=15, verbose_name="Tipo de Usuario", blank=False, null=False)

    def __str__(self) -> str:
        return self.descripcion

class Usuario(models.Model):
    rutUsu = models.CharField(primary_key=True,max_length=20, verbose_name="Rut del Usuario")
    nombreUsu = models.CharField(max_length=50, verbose_name="Nombre del Usuario", blank=False, null=False)
    apellidoUsu = models.CharField(max_length=50, verbose_name="Apellido del Usuario", blank=False, null=False)
    correoUsu = models.CharField(max_length=100, verbose_name="Correo del Usuario", blank=False, null=False)
    contrasenaUsu = models.CharField(max_length=50, verbose_name="Contraseña del Usuario", blank=False, null=False)
    telefonoUsu = models.IntegerField(verbose_name="Telefono del Usuario", blank=False, null=False)
    tipousuario = models.ForeignKey(TipoUsuario, on_delete=CASCADE)

    def __str__(self) -> str:
        return self.nombreUsu + " " + self.apellidoUsu

class Direccion(models.Model):
    idDireccion = models.AutoField(primary_key=True, verbose_name="Id de la Direccion")
    descripcion = models.CharField(max_length=50, verbose_name="Direccion", blank=False, null=False)
    numDic = models.IntegerField(verbose_name="Número de la Dirección")
    blockDpto = models.CharField(max_length=5, verbose_name="Bloque del Departamento")
    numDpto = models.CharField(max_length=5, verbose_name="Número del Departamento")
    direccionDespacho = models.IntegerField(verbose_name="Corresponde a Direccion de Despacho", blank=False, null=False)
    comuna = models.ForeignKey(Comuna, on_delete=CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=CASCADE)

    def __str__(self) -> str:
        return self.descripcion + " #" + self.numDic

class Venta(models.Model):
    factura = models.AutoField(primary_key=True, verbose_name="Número de la Factura")
    fechaVenta = models.DateField(verbose_name="Fecha de la Factura", blank=False, null=False)
    total = models.IntegerField(verbose_name= "Total de la Factura", blank=False, null=False)
    estado = models.IntegerField(verbose_name="Estado de la Factura", blank=False, null=False)
    usuario = models.ForeignKey(Usuario, on_delete=CASCADE)
    direccion = models.ForeignKey(Direccion, on_delete=CASCADE)


class TipoProducto(models.Model):
    idTipoProd = models.AutoField(primary_key=True, verbose_name="Id del Tipo de Producto")
    descripcion = models.CharField(max_length=30, verbose_name="Tipo de Producto", blank=False, null=False)

    def __str__(self) -> str:
        return self.descripcion

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True, verbose_name="Id del Producto")
    nombreProd = models.CharField(max_length=30, verbose_name="Nombre del Producto", blank=False, null=False)
    precioProd = models.IntegerField(verbose_name= "Precio del Producto", blank=False, null=False)
    descripcionProd = models.CharField(max_length=200, verbose_name="Descripcion del Producto", blank=False, null=False)
    fotoProd = models.ImageField(verbose_name="Foto", blank=False, null=False)
    stockProd = models.IntegerField(verbose_name= "Stock del Producto", blank=False, null=False)
    tipoproducto = models.ForeignKey(TipoProducto, on_delete=CASCADE)
    tallaProd = models.CharField(max_length=3, verbose_name="Talla del Producto", blank=False, null=False)
    colorProd = models.CharField(max_length=10, verbose_name="Color del Producto", blank=False, null=False)

    def __str__(self) -> str:
        return self.nombreProd

class DetalleVenta(models.Model):
    idDetalle = models.AutoField(primary_key=True, verbose_name="Id del Detalle de la Venta")
    cantidadProd = models.IntegerField(verbose_name="Cantidad de Productos", blank=False, null=False)
    venta = models.ForeignKey(Venta, on_delete=CASCADE)
    subTotalDet = models.IntegerField(verbose_name="Subtotal del Detalle", blank=False, null=False)
    producto = models.ForeignKey(Producto, on_delete=CASCADE)

class Contactanos(models.Model):
    idContac = models.AutoField(primary_key=True, verbose_name="Id del Contactanos")
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Usuario", blank=False, null=False)
    correo = models.CharField(max_length=100, verbose_name="Correo del Usuario", blank=False, null=False)
    asunto = models.CharField(max_length=50, verbose_name="Asunto del Contactanos", blank=False, null=False)
    comentario = models.CharField(max_length=500, verbose_name="Comentario del Contactanos", blank=False, null=False)
    visto = models.IntegerField(verbose_name="El Mensaje fue Leído", blank=False, null=False)

    def __str__(self) -> str:
        return self.nombre
