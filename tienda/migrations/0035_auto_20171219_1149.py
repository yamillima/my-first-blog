# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0034_auto_20171218_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='correo_electronico',
            field=models.CharField(max_length=200, default='desconocido'),
        ),
        migrations.AlterField(
            model_name='chico',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 19, 11, 49, 43, 444125)),
        ),
        migrations.AlterField(
            model_name='dama',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 19, 11, 49, 43, 441125)),
        ),
        migrations.AlterField(
            model_name='hombre',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 19, 11, 49, 43, 443125)),
        ),
        migrations.AlterField(
            model_name='visita',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 19, 11, 49, 43, 440125)),
        ),
    ]
