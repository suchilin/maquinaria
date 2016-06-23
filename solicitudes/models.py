from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Solicitudes(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    identificador = models.IntegerField(db_column='IDENTIFICADOR', blank=True, null=True)  # Field name made lowercase.
    delegacion = models.TextField(db_column='DELEGACION', blank=True, null=True)  # Field name made lowercase.
    tipo_apoyo = models.TextField(db_column='TIPO APOYO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    curp = models.TextField(db_column='CURP', blank=True, null=True)  # Field name made lowercase.
    folio = models.TextField(db_column='FOLIO', blank=True, null=True)  # Field name made lowercase.
    nombre = models.TextField(db_column='NOMBRE', blank=True, null=True)  # Field name made lowercase.
    rfc = models.TextField(db_column='RFC', blank=True, null=True)  # Field name made lowercase.
    ddr = models.TextField(db_column='DDR', blank=True, null=True)  # Field name made lowercase.
    cader = models.TextField(db_column='CADER', blank=True, null=True)  # Field name made lowercase.
    municipio = models.TextField(db_column='MUNICIPIO', blank=True, null=True)  # Field name made lowercase.
    localidad = models.TextField(db_column='LOCALIDAD', blank=True, null=True)  # Field name made lowercase.
    beneficio = models.TextField(db_column='BENEFICIO', blank=True, null=True)  # Field name made lowercase.
    concepto = models.TextField(db_column='CONCEPTO', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.FloatField(db_column='CANTIDAD', blank=True, null=True)  # Field name made lowercase.
    precio_unitario = models.FloatField(db_column='PRECIO UNITARIO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    inversion_total = models.FloatField(db_column='INVERSION TOTAL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    apoyo_federal_dictaminado = models.FloatField(db_column='APOYO FEDERAL DICTAMINADO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    marca = models.TextField(db_column='MARCA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    modelo = models.TextField(db_column='MODELO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rfc_proovedor = models.TextField(db_column='RFC PROOVEDOR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    proveedor = models.TextField(db_column='PROVEEDOR', blank=True, null=True)  # Field name made lowercase.
    monto_autorizado = models.FloatField(db_column='MONTO AUTORIZADO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    factura = models.TextField(db_column='FACTURA', blank=True, null=True)  # Field name made lowercase.
    fecha_factura = models.TextField(db_column='FECHA FACTURA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nombre_de_banco = models.TextField(db_column='NOMBRE DE BANCO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    clabe = models.TextField(db_column='CLABE', blank=True, null=True)  # Field name made lowercase.
    sol_status = models.TextField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    fact = models.BooleanField(db_column='FACT', default=False)  # Field name made lowercase.
    carta_pago_terceros = models.BooleanField(db_column='CARTA PAGO TERCEROS', default=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reporte_verif = models.BooleanField(db_column='REPORTE VERIF', default=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    carta_entrega_recepcion = models.BooleanField(db_column='CARTA ENTREGA-RECEPCION', default=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    oservaciones = models.TextField(db_column='OSERVACIONES', blank=True, null=True)  # Field name made lowercase.

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Solicitudes'
        verbose_name = 'Solicitud'
        db_table = 'solicitudes'


class ProvProfile(models.Model):
    user = models.OneToOneField(User, related_name='perfil')
    es_moral = models.BooleanField(db_column='MORAL', default=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    escritura = models.CharField(db_column='ESCRITURA', max_length=100)  # Field name made lowercase.
    escritura_fecha = models.CharField(db_column='ESCRITURA FECHA', max_length=100)  # Field name made lowercase.
    escritura_notario = models.CharField(db_column='ESCRITURA NOTARIO', max_length=100)  # Field name made lowercase.
    escritura_notario_numero = models.CharField(db_column='ESCRITURA NOTARIO NUMERO', max_length=100)  # Field name made lowercase.
    escritura_notario_ciudad = models.CharField(db_column='ESCRITURA NOTARIO CIUDAD', max_length=100)  # Field name made lowercase.
    apoderado_legal = models.CharField(db_column='APODERADO LEGAL', max_length=100)  # Field name made lowercase.
    apoderado_legal_domicilio = models.CharField(db_column='APODERADO LEGAL DOMICILIO', max_length=100)  # Field name made lowercase.
    poder = models.CharField(db_column='PODER', max_length=100)  # Field name made lowercase.
    poder_fecha = models.CharField(db_column='PODER FECHA', max_length=100)  # Field name made lowercase.
    poder_ciudad = models.CharField(db_column='PODER CIUDAD', max_length=100)  # Field name made lowercase.
    poder_notario = models.CharField(db_column='PODER NOTARIO', max_length=100)  # Field name made lowercase.
    poder_notario_numero = models.CharField(db_column='PODER NOTARIO NUMERO', max_length=100)  # Field name made lowercase.
    nombre_cuentahabiente = models.CharField(db_column='NOMBRE CUENTAHABIENTE', max_length=100)  # Field name made lowercase.
    nombre_banco = models.CharField(db_column='NOMBRE BANCO', max_length=100)  # Field name made lowercase.
    clave_banco = models.CharField(db_column='CLAVE BANCO', max_length=3)  # Field name made lowercase.
    clabe_interbancaria = models.CharField(db_column='CLABE INTERBANCARIA', max_length=100)  # Field name made lowercase.

