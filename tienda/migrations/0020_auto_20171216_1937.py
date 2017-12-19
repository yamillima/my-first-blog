# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0019_auto_20171216_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chico',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 16, 19, 37, 21, 646329)),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 16, 19, 37, 21, 646329)),
        ),
        migrations.AlterField(
            model_name='compra',
            name='telefono_del_comprador',
            field=models.IntegerField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='dama',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 16, 19, 37, 21, 646329)),
        ),
        migrations.AlterField(
            model_name='hombre',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 16, 19, 37, 21, 646329)),
        ),
        migrations.AlterField(
            model_name='visita',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 16, 19, 37, 21, 646329)),
        ),
    ]
