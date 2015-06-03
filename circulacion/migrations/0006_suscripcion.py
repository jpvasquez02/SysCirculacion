# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0005_auto_20150602_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='suscripcion',
            fields=[
                ('Codigo', models.IntegerField(primary_key=True, serialize=False, max_length=10)),
                ('Categoria', models.CharField(choices=[('Empresarial', 'Empresarial'), ('Residencial', 'Residencial')], max_length=50)),
                ('Cantidad', models.IntegerField(max_length=5)),
                ('Descuento', models.DecimalField(max_digits=5, decimal_places=2)),
                ('Valor', models.DecimalField(max_digits=8, decimal_places=2)),
                ('Contrato', models.IntegerField()),
                ('Recibo', models.IntegerField()),
                ('Entrega', models.CharField(choices=[('L-D', 'L-D'), ('L-S', 'L-S'), ('L-V', 'L-V')], max_length=5)),
                ('Comentarios', models.TextField()),
                ('Tipo', models.CharField(choices=[('Canje', 'Canje'), ('Certificado', 'Certificado'), ('Cortesia', 'Cortesia'), ('DxP', 'Deducible Por Planilla'), ('Pagado', 'Pagado')], max_length=35)),
                ('Inicio', models.DateField()),
                ('Fin', models.DateField()),
                ('Asesor', models.ForeignKey(to='circulacion.asesores')),
                ('Plan', models.ForeignKey(to='circulacion.planes')),
                ('Repartidor', models.ForeignKey(to='circulacion.repartidores')),
                ('Ruta', models.ForeignKey(to='circulacion.rutas')),
                ('Suscriptor', models.ForeignKey(to='circulacion.clientes')),
            ],
            options={
                'verbose_name_plural': 'Suscripciones',
                'ordering': ['Codigo', 'Suscriptor'],
            },
            bases=(models.Model,),
        ),
    ]
