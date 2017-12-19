# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0031_auto_20171218_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chico',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 18, 18, 51, 48, 127443)),
        ),
        migrations.AlterField(
            model_name='compra',
            name='precio',
            field=models.CharField(max_length=200, blank=True, null=True, default='desconocido'),
        ),
        migrations.AlterField(
            model_name='dama',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 18, 18, 51, 48, 127443)),
        ),
        migrations.AlterField(
            model_name='hombre',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 18, 18, 51, 48, 127443)),
        ),
        migrations.AlterField(
            model_name='visita',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 18, 18, 51, 48, 127443)),
        ),
    ]
