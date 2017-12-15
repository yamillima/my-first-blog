# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 00:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0006_auto_20171202_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hombre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=datetime.datetime(2017, 12, 2, 19, 19, 16, 125101))),
            ],
        ),
        migrations.AlterField(
            model_name='dama',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 2, 19, 19, 16, 121100)),
        ),
        migrations.AlterField(
            model_name='visita',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 2, 19, 19, 16, 119100)),
        ),
    ]
