# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0010_auto_20150603_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repartidores',
            name='Telefono',
            field=models.CharField(blank=True, max_length=10, null=True),
            preserve_default=True,
        ),
    ]
