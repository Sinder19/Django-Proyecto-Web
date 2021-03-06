# Generated by Django 3.2.3 on 2021-06-24 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AmonStore', '0005_carrito_totalprod'),
    ]

    operations = [
        migrations.CreateModel(
            name='MensajeVisto',
            fields=[
                ('idTipo', models.AutoField(primary_key=True, serialize=False, verbose_name='Id del tipo de visto')),
                ('descripcion', models.CharField(max_length=30, verbose_name='Descripcion del tipo de visto')),
            ],
        ),
        migrations.AddField(
            model_name='contactanos',
            name='mensajevisto',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='AmonStore.mensajevisto'),
            preserve_default=False,
        ),
    ]
