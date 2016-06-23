# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='provprofile',
            name='clabe_interbancaria',
            field=models.CharField(default='', max_length=100, db_column='CLABE INTERBANCARIA'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provprofile',
            name='clave_banco',
            field=models.CharField(default='', max_length=3, db_column='CLAVE BANCO'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provprofile',
            name='nombre_cuentahabiente',
            field=models.CharField(default='', max_length=100, db_column='NOMBRE CUENTAHABIENTE'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='provprofile',
            name='apoderado_legal',
            field=models.CharField(max_length=100, db_column='APODERADO LEGAL'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provprofile',
            name='apoderado_legal_domicilio',
            field=models.CharField(max_length=100, db_column='APODERADO LEGAL DOMICILIO'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provprofile',
            name='escritura_fecha',
            field=models.CharField(max_length=100, db_column='ESCRITURA FECHA'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provprofile',
            name='escritura_notario',
            field=models.CharField(max_length=100, db_column='ESCRITURA NOTARIO'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provprofile',
            name='escritura_notario_ciudad',
            field=models.CharField(max_length=100, db_column='ESCRITURA NOTARIO CIUDAD'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provprofile',
            name='escritura_notario_numero',
            field=models.CharField(max_length=100, db_column='ESCRITURA NOTARIO NUMERO'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provprofile',
            name='nombre_banco',
            field=models.CharField(max_length=100, db_column='NOMBRE BANCO'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provprofile',
            name='poder',
            field=models.CharField(max_length=100, db_column='PODER'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provprofile',
            name='poder_ciudad',
            field=models.CharField(max_length=100, db_column='PODER CIUDAD'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provprofile',
            name='poder_fecha',
            field=models.CharField(max_length=100, db_column='PODER FECHA'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provprofile',
            name='poder_notario',
            field=models.CharField(max_length=100, db_column='PODER NOTARIO'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provprofile',
            name='poder_notario_numero',
            field=models.CharField(max_length=100, db_column='PODER NOTARIO NUMERO'),
            preserve_default=True,
        ),
    ]
