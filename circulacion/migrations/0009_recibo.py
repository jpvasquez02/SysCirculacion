# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulacion', '0008_cierre_tiraje'),
    ]

    operations = [
        migrations.CreateModel(
            name='recibo',
            fields=[
                ('Codigo', models.AutoField(serialize=False, primary_key=True)),
                ('Fecha', models.DateField()),
                ('Tipo', models.CharField(choices=[('Canje', 'Canje'), ('Certificado', 'Certificado'), ('Cortesia', 'Cortesia'), ('DxP', 'Deducible Por Planilla'), ('Pagado', 'Pagado')], max_length=35)),
                ('Descripcion', models.TextField()),
                ('Valor', models.DecimalField(max_digits=8, decimal_places=2)),
                ('Nombre', models.ForeignKey(to='circulacion.suscripcion')),
                ('Plan', models.ForeignKey(to='circulacion.planes')),
            ],
            options={
                'verbose_name_plural': 'Recibos',
                'ordering': ['Codigo', 'Fecha'],
            },
            bases=(models.Model,),
        ),
    ]
