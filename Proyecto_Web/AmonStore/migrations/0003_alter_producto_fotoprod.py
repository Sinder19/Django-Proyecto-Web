# Generated by Django 3.2.3 on 2021-06-05 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AmonStore', '0002_auto_20210605_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fotoProd',
            field=models.ImageField(upload_to='productos', verbose_name='Foto'),
        ),
    ]