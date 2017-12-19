# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0018_auto_20171216_1228'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pedido',
        ),
        migrations.AddField(
            model_name='compra',
            name='direccion_de_entrega',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='compra',
            name='fecha_de_entrega',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='compra',
            name='hora_de_entrega',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='compra',
            name='nombre_del_comprador',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='compra',
            name='nombre_del_destinatario',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='compra',
            name='telefono_del_comprador',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='chico',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 16, 18, 21, 53, 974868)),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 16, 18, 21, 53, 974868)),
        ),
        migrations.AlterField(
            model_name='dama',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 16, 18, 21, 53, 957268)),
        ),
        migrations.AlterField(
            model_name='hombre',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 16, 18, 21, 53, 957268)),
        ),
        migrations.AlterField(
            model_name='visita',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 16, 18, 21, 53, 957268)),
        ),
    ]
