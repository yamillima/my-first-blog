# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-15 23:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0011_auto_20171215_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chico',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 15, 18, 30, 3, 701676)),
        ),
        migrations.AlterField(
            model_name='dama',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 15, 18, 30, 3, 698676)),
        ),
        migrations.AlterField(
            model_name='hombre',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 15, 18, 30, 3, 699676)),
        ),
        migrations.AlterField(
            model_name='visita',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 15, 18, 30, 3, 697676)),
        ),
    ]
