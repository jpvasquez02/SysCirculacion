# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0011_auto_20150610_0929'),
    ]

    operations = [
        migrations.CreateModel(
            name='colonias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('Nombre', models.CharField(max_length=30)),
                ('Nse', models.CharField(blank=True, max_length=5, null=True)),
            ],
            options={
                'ordering': ['Nombre'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='punto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('Codigo', models.IntegerField(max_length=10)),
                ('Nombre', models.CharField(max_length=140)),
                ('Lunes', models.IntegerField(max_length=5)),
                ('Martes', models.IntegerField(max_length=5)),
                ('Miercoles', models.IntegerField(max_length=5)),
                ('Jueves', models.IntegerField(max_length=5)),
                ('Viernes', models.IntegerField(max_length=5)),
                ('Sabado', models.IntegerField(max_length=5)),
                ('Domingo', models.IntegerField(max_length=5)),
                ('Ruta', models.ForeignKey(to='circulacion.rutas')),
                ('Supervisor', models.ForeignKey(blank=True, to='circulacion.supervisores', null=True)),
            ],
            options={
                'ordering': ['Ruta', 'Supervisor'],
                'verbose_name_plural': 'Punto de Venta',
            },
            bases=(models.Model,),
        ),
    ]
