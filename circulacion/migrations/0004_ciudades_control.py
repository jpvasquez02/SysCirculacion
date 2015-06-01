# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0003_auto_20150601_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='ciudades',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Municipio', models.CharField(max_length=140)),
                ('Departamento', models.ForeignKey(to='circulacion.departamentos')),
            ],
            options={
                'ordering': ['Departamento'],
                'verbose_name_plural': 'Ciudades',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='control',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Fecha', models.DateField()),
                ('Motivo', models.CharField(choices=[(1, 'Faltaron X Vendedores'), (2, 'Semaforo en mal Estado'), (3, 'Falta de Energía Eléctrica'), (4, 'Calle Cerrada'), (5, 'Manifestacion')], max_length=140)),
                ('Comentarios', models.TextField(null=True, blank=True)),
                ('Supervisor', models.ForeignKey(to='circulacion.supervisores')),
            ],
            options={
                'ordering': ['Fecha'],
                'verbose_name_plural': 'Hoja de Control',
            },
            bases=(models.Model,),
        ),
    ]
