# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0035_auto_20171219_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('nombre', models.CharField(max_length=200)),
                ('correo_electronico', models.CharField(max_length=200)),
                ('comentario', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='chico',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 19, 17, 36, 24, 769918)),
        ),
        migrations.AlterField(
            model_name='compra',
            name='correo_electronico',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='dama',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 19, 17, 36, 24, 754318)),
        ),
        migrations.AlterField(
            model_name='hombre',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 19, 17, 36, 24, 754318)),
        ),
        migrations.AlterField(
            model_name='visita',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 19, 17, 36, 24, 754318)),
        ),
    ]
