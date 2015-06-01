# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='planes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('CodigoPlan', models.CharField(max_length=4)),
                ('Nombre', models.CharField(max_length=50)),
                ('Precio', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
            options={
                'verbose_name_plural': 'Planes',
                'ordering': ['CodigoPlan'],
            },
            bases=(models.Model,),
        ),
    ]
