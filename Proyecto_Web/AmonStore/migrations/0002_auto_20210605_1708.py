# Generated by Django 3.2.3 on 2021-06-05 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AmonStore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccion',
            name='direccionDespacho',
            field=models.IntegerField(verbose_name='Corresponde a Direccion de Despacho'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='colorProd',
            field=models.CharField(max_length=10, verbose_name='Color del Producto'),
        ),
    ]