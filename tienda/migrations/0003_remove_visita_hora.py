# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 17:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_visita'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visita',
            name='hora',
        ),
    ]
