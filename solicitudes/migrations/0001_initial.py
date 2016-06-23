# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProvProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('es_moral', models.BooleanField(default=True, db_column='MORAL')),
                ('escritura', models.CharField(max_length=100, db_column='ESCRITURA')),
                ('escritura_fecha', models.TextField(db_column='ESCRITURA FECHA')),
                ('escritura_notario', models.TextField(db_column='ESCRITURA NOTARIO')),
                ('escritura_notario_numero', models.TextField(db_column='ESCRITURA NOTARIO NUMERO')),
                ('escritura_notario_ciudad', models.TextField(db_column='ESCRITURA NOTARIO CIUDAD')),
                ('apoderado_legal', models.TextField(db_column='APODERADO LEGAL')),
                ('apoderado_legal_domicilio', models.TextField(db_column='APODERADO LEGAL DOMICILIO')),
                ('poder', models.TextField(db_column='PODER')),
                ('poder_fecha', models.TextField(db_column='PODER FECHA')),
                ('poder_ciudad', models.TextField(db_column='PODER CIUDAD')),
                ('poder_notario', models.TextField(db_column='PODER NOTARIO')),
                ('poder_notario_numero', models.TextField(db_column='PODER NOTARIO NUMERO')),
                ('nombre_banco', models.TextField(db_column='NOMBRE BANCO')),
                ('user', models.OneToOneField(related_name='perfil', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Solicitudes',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='Id')),
                ('identificador', models.IntegerField(null=True, db_column='IDENTIFICADOR', blank=True)),
                ('delegacion', models.TextField(null=True, db_column='DELEGACION', blank=True)),
                ('tipo_apoyo', models.TextField(null=True, db_column='TIPO APOYO', blank=True)),
                ('curp', models.TextField(null=True, db_column='CURP', blank=True)),
                ('folio', models.TextField(null=True, db_column='FOLIO', blank=True)),
                ('nombre', models.TextField(null=True, db_column='NOMBRE', blank=True)),
                ('rfc', models.TextField(null=True, db_column='RFC', blank=True)),
                ('ddr', models.TextField(null=True, db_column='DDR', blank=True)),
                ('cader', models.TextField(null=True, db_column='CADER', blank=True)),
                ('municipio', models.TextField(null=True, db_column='MUNICIPIO', blank=True)),
                ('localidad', models.TextField(null=True, db_column='LOCALIDAD', blank=True)),
                ('beneficio', models.TextField(null=True, db_column='BENEFICIO', blank=True)),
                ('concepto', models.TextField(null=True, db_column='CONCEPTO', blank=True)),
                ('cantidad', models.FloatField(null=True, db_column='CANTIDAD', blank=True)),
                ('precio_unitario', models.FloatField(null=True, db_column='PRECIO UNITARIO', blank=True)),
                ('inversion_total', models.FloatField(null=True, db_column='INVERSION TOTAL', blank=True)),
                ('apoyo_federal_dictaminado', models.FloatField(null=True, db_column='APOYO FEDERAL DICTAMINADO', blank=True)),
                ('marca', models.TextField(null=True, db_column='MARCA', blank=True)),
                ('modelo', models.TextField(null=True, db_column='MODELO', blank=True)),
                ('rfc_proovedor', models.TextField(null=True, db_column='RFC PROOVEDOR', blank=True)),
                ('proveedor', models.TextField(null=True, db_column='PROVEEDOR', blank=True)),
                ('monto_autorizado', models.FloatField(null=True, db_column='MONTO AUTORIZADO', blank=True)),
                ('factura', models.TextField(null=True, db_column='FACTURA', blank=True)),
                ('fecha_factura', models.TextField(null=True, db_column='FECHA FACTURA', blank=True)),
                ('nombre_de_banco', models.TextField(null=True, db_column='NOMBRE DE BANCO', blank=True)),
                ('clabe', models.TextField(null=True, db_column='CLABE', blank=True)),
                ('sol_status', models.TextField(null=True, db_column='STATUS', blank=True)),
                ('fact', models.BooleanField(default=False, db_column='FACT')),
                ('carta_pago_terceros', models.BooleanField(default=False, db_column='CARTA PAGO TERCEROS')),
                ('reporte_verif', models.BooleanField(default=False, db_column='REPORTE VERIF')),
                ('carta_entrega_recepcion', models.BooleanField(default=False, db_column='CARTA ENTREGA-RECEPCION')),
                ('oservaciones', models.TextField(null=True, db_column='OSERVACIONES', blank=True)),
            ],
            options={
                'db_table': 'solicitudes',
                'verbose_name': 'Solicitud',
                'verbose_name_plural': 'Solicitudes',
            },
            bases=(models.Model,),
        ),
    ]
