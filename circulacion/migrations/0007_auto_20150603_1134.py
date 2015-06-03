# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0006_suscripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suscripcion',
            name='Descuento',
            field=models.DecimalField(decimal_places=2, blank=True, max_digits=5, null=True),
            preserve_default=True,
        ),
    ]
