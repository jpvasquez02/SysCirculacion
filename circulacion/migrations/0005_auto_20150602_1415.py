# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0004_ciudades_control'),
    ]

    operations = [
        migrations.CreateModel(
            name='clientes',
            fields=[
                ('Codigo', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('TipoCliente', models.CharField(choices=[('Empresarial', 'Empresarial'), ('Residencial', 'Residencial')], max_length=50)),
                ('Nombre', models.CharField(max_length=140)),
                ('Identificacion', models.CharField(max_length=15)),
                ('FechaNacimiento', models.DateField()),
                ('Genero', models.CharField(null=True, blank=True, max_length=15, choices=[('F', 'Femenino'), ('M', 'Masculino')])),
                ('Telefono', models.IntegerField(null=True, blank=True, max_length=15)),
                ('Celular', models.IntegerField(null=True, blank=True, max_length=15)),
                ('Colonia', models.CharField(max_length=140)),
                ('Calle', models.CharField(max_length=30)),
                ('Avenida', models.CharField(max_length=30)),
                ('Referencia', models.CharField(max_length=140)),
                ('Correo', models.EmailField(max_length=75)),
                ('latitud', models.CharField(max_length=50)),
                ('longitud', models.CharField(max_length=50)),
                ('Ciudad', models.ForeignKey(to='circulacion.ciudades')),
                ('Departamento', models.ForeignKey(to='circulacion.departamentos')),
            ],
            options={
                'verbose_name_plural': 'Clientes',
                'ordering': ['Nombre'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='empleados',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=140)),
                ('Puesto', models.CharField(max_length=140)),
            ],
            options={
                'verbose_name_plural': 'Empleados',
                'ordering': ['Nombre'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='repartidores',
            name='Telefono',
            field=models.CharField(null=True, blank=True, max_length=15),
            preserve_default=True,
        ),
    ]
