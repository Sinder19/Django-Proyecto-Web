from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.utils import serializer_helpers
from .serializers import ProductoSerializador
from AmonStore.models import Producto

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@csrf_exempt

@api_view(['GET'])
def ver_productos(request):
    if request.method == 'GET':
        p = Producto.objects.all()
        serializer = ProductoSerializador(p, many = True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def agregar_producto(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializador(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
@permission_classes((IsAuthenticated,))
def modificar_producto(request, id):
    try:
        p = Producto.objects.get(idProducto = id)
    except Producto.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductoSerializador(p)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductoSerializador(p, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
@permission_classes((IsAuthenticated,))
def eliminar_producto(request, id):
    try:
        p = Producto.objects.get(idProducto = id)
    except Producto.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductoSerializador(p)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        p.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)