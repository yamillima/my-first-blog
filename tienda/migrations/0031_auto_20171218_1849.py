# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0030_auto_20171218_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chico',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 18, 18, 49, 55, 526564)),
        ),
        migrations.AlterField(
            model_name='compra',
            name='precio',
            field=models.CharField(max_length=200, default='desconocido'),
        ),
        migrations.AlterField(
            model_name='dama',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 18, 18, 49, 55, 481561)),
        ),
        migrations.AlterField(
            model_name='hombre',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 18, 18, 49, 55, 525564)),
        ),
        migrations.AlterField(
            model_name='visita',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 18, 18, 49, 55, 479561)),
        ),
    ]
