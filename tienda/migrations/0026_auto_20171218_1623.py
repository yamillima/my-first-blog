# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0025_auto_20171217_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='comprarclick',
            name='producto',
            field=models.CharField(max_length=200, default='sin definir'),
        ),
        migrations.AlterField(
            model_name='chico',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 18, 16, 23, 16, 995980)),
        ),
        migrations.AlterField(
            model_name='compra',
            name='regalo',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='compra',
            name='telefono_del_comprador',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='dama',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 18, 16, 23, 16, 992980)),
        ),
        migrations.AlterField(
            model_name='hombre',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 18, 16, 23, 16, 993980)),
        ),
        migrations.AlterField(
            model_name='visita',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 18, 16, 23, 16, 990979)),
        ),
    ]
