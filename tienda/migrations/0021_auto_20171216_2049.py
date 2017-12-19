# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0020_auto_20171216_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chico',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 16, 20, 49, 6, 729772)),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 17, 1, 49, 6, 729772, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='compra',
            name='telefono_del_comprador',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dama',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 16, 20, 49, 6, 729772)),
        ),
        migrations.AlterField(
            model_name='hombre',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 16, 20, 49, 6, 729772)),
        ),
        migrations.AlterField(
            model_name='visita',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 16, 20, 49, 6, 729772)),
        ),
    ]
