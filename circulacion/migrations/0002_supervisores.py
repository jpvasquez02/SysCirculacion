# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='supervisores',
            fields=[
                ('Codigo', models.IntegerField(serialize=False, max_length=10, primary_key=True)),
                ('Nombre', models.CharField(max_length=140)),
            ],
            options={
                'verbose_name_plural': 'Supervisores',
            },
            bases=(models.Model,),
        ),
    ]
