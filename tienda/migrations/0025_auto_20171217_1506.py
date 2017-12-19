# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0024_auto_20171217_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='regalo',
            field=models.CharField(max_length=200, default='regalo'),
        ),
        migrations.AlterField(
            model_name='chico',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 17, 15, 6, 13, 337768)),
        ),
        migrations.AlterField(
            model_name='dama',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 17, 15, 6, 13, 332768)),
        ),
        migrations.AlterField(
            model_name='hombre',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 17, 15, 6, 13, 336768)),
        ),
        migrations.AlterField(
            model_name='visita',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 17, 15, 6, 13, 331768)),
        ),
    ]
