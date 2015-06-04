# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0009_recibo'),
    ]

    operations = [
        migrations.CreateModel(
            name='guia',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('Fecha', models.DateField()),
                ('Dia', models.CharField(choices=[('L', 'Lunes'), ('M', 'Martes'), ('K', 'Miercoles'), ('J', 'Jueves'), ('V', 'Viernes'), ('S', 'Sabado'), ('D', 'Domingo')], max_length=10)),
                ('Destino', models.CharField(max_length=140, blank=True, null=True)),
                ('Envios', models.IntegerField(max_length=5, blank=True, null=True)),
                ('Cortesias', models.IntegerField(max_length=5, blank=True, null=True)),
                ('Suscripciones', models.IntegerField(max_length=5, blank=True, null=True)),
                ('Cliente', models.ForeignKey(to='circulacion.suscripcion')),
                ('Ruta', models.ForeignKey(to='circulacion.rutas')),
                ('Supervisor', models.ForeignKey(blank=True, to='circulacion.supervisores', null=True)),
            ],
            options={
                'verbose_name_plural': 'Guía de Producción',
                'ordering': ['Ruta'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='tiraje',
            options={'verbose_name_plural': 'Tiraje', 'ordering': ['Ruta']},
        ),
    ]
