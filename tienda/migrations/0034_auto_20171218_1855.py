# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0033_auto_20171218_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chico',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 18, 18, 54, 22, 808491)),
        ),
        migrations.AlterField(
            model_name='compra',
            name='direccion_de_entrega',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_de_entrega',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='compra',
            name='hora_de_entrega',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='compra',
            name='nombre_del_comprador',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='compra',
            name='nombre_del_destinatario',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='compra',
            name='precio',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='compra',
            name='telefono_del_comprador',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='dama',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 18, 18, 54, 22, 792891)),
        ),
        migrations.AlterField(
            model_name='hombre',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 18, 18, 54, 22, 808491)),
        ),
        migrations.AlterField(
            model_name='visita',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 18, 18, 54, 22, 792891)),
        ),
    ]
