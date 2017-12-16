# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0015_auto_20171215_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fecha', models.DateTimeField(default=datetime.datetime(2017, 12, 15, 23, 53, 22, 882383))),
            ],
        ),
        migrations.AlterField(
            model_name='chico',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 15, 23, 53, 22, 882383)),
        ),
        migrations.AlterField(
            model_name='dama',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 15, 23, 53, 22, 882383)),
        ),
        migrations.AlterField(
            model_name='hombre',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 15, 23, 53, 22, 882383)),
        ),
        migrations.AlterField(
            model_name='visita',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 15, 23, 53, 22, 882383)),
        ),
    ]
