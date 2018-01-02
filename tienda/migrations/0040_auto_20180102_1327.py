# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0039_auto_20171231_0855'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tendero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='chico',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 2, 13, 27, 48, 793464)),
        ),
        migrations.AlterField(
            model_name='dama',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 2, 13, 27, 48, 793464)),
        ),
        migrations.AlterField(
            model_name='hombre',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 2, 13, 27, 48, 793464)),
        ),
        migrations.AlterField(
            model_name='producto',
            name='vendedor',
            field=models.ForeignKey(blank=True, to='tienda.Tendero'),
        ),
        migrations.AlterField(
            model_name='visita',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 2, 13, 27, 48, 777864)),
        ),
    ]
