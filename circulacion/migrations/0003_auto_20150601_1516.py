# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0002_supervisores'),
    ]

    operations = [
        migrations.CreateModel(
            name='asesores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('NombreAsesor', models.CharField(max_length=140)),
            ],
            options={
                'verbose_name_plural': 'Asesores',
                'ordering': ['NombreAsesor'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='departamentos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('Departamento', models.CharField(max_length=140)),
            ],
            options={
                'verbose_name_plural': 'Departamentos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='repartidores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('NombreRepartidor', models.CharField(max_length=140)),
                ('Telefono', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Repartidores',
                'ordering': ['NombreRepartidor'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='rutas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('NombreRuta', models.CharField(max_length=35)),
                ('Colonias', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Rutas',
                'ordering': ['NombreRuta'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='planes',
            options={'verbose_name_plural': 'Planes', 'ordering': ['CodigoPlan', 'Nombre', 'Precio']},
        ),
    ]
