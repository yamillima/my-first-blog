# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0017_auto_20171216_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='direccion_de_entrega',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='fecha_de_entrega',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='hora_de_entrega',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='nombre_del_comprador',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='nombre_del_destinatario',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='telefono_del_comprador',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='chico',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 16, 12, 28, 22, 894820)),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 16, 12, 28, 22, 897820)),
        ),
        migrations.AlterField(
            model_name='dama',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 16, 12, 28, 22, 890819)),
        ),
        migrations.AlterField(
            model_name='hombre',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 16, 12, 28, 22, 891819)),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 16, 12, 28, 22, 899820)),
        ),
        migrations.AlterField(
            model_name='visita',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 16, 12, 28, 22, 888819)),
        ),
    ]
