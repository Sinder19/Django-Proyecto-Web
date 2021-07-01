from django.db.models import fields
from django.db.models.base import Model
from AmonStore.models import Producto
from rest_framework import serializers

class ProductoSerializador(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombreProd', 'precioProd', 'descripcionProd', 'stockProd', 'tipoproducto', 'tallaProd', 'colorProd']
    