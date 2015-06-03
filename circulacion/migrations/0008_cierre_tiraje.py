# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0007_auto_20150603_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='cierre',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('Cantidad', models.IntegerField(max_length=5)),
                ('Direccion', models.CharField(max_length=140)),
                ('Valor', models.DecimalField(max_digits=8, decimal_places=2)),
                ('Recibo', models.CharField(max_length=10)),
                ('ValorRecibido', models.DecimalField(max_digits=8, decimal_places=2)),
                ('Comision', models.DecimalField(max_digits=8, decimal_places=2)),
                ('FechaPago', models.DateField()),
                ('Inicio', models.DateField()),
                ('Fin', models.DateField()),
                ('Nombre', models.ForeignKey(to='circulacion.suscripcion')),
                ('Tipo', models.ForeignKey(to='circulacion.planes')),
                ('Vendedor', models.ForeignKey(to='circulacion.empleados')),
            ],
            options={
                'verbose_name_plural': 'Cierre Circulación',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='tiraje',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('Lunes', models.IntegerField(max_length=5)),
                ('Martes', models.IntegerField(max_length=5)),
                ('Miercoles', models.IntegerField(max_length=5)),
                ('Jueves', models.IntegerField(max_length=5)),
                ('Viernes', models.IntegerField(max_length=5)),
                ('Sabado', models.IntegerField(max_length=5)),
                ('Domingo', models.IntegerField(max_length=5)),
                ('Ruta', models.ForeignKey(to='circulacion.rutas')),
            ],
            options={
                'verbose_name_plural': 'Plural',
                'ordering': ['Ruta'],
            },
            bases=(models.Model,),
        ),
    ]
