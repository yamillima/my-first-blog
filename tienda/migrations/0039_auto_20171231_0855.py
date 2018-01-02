# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0038_auto_20171229_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='vendedor',
            field=models.EmailField(max_length=254, default='yamilandreslima@gmail.com'),
        ),
        migrations.AlterField(
            model_name='chico',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 31, 8, 55, 13, 468130)),
        ),
        migrations.AlterField(
            model_name='dama',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 31, 8, 55, 13, 465130)),
        ),
        migrations.AlterField(
            model_name='hombre',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 31, 8, 55, 13, 467130)),
        ),
        migrations.AlterField(
            model_name='visita',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 31, 8, 55, 13, 462130)),
        ),
    ]
