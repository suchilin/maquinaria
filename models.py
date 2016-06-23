# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Solicitudes(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    identificador = models.IntegerField(db_column='IDENTIFICADOR', blank=True, null=True)  # Field name made lowercase.
    delegacion = models.TextField(db_column='DELEGACION', blank=True)  # Field name made lowercase.
    tipo_apoyo = models.TextField(db_column='TIPO APOYO', blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    folio = models.TextField(db_column='FOLIO', blank=True)  # Field name made lowercase.
    nombre = models.TextField(db_column='NOMBRE', blank=True)  # Field name made lowercase.
    curp = models.TextField(db_column='CURP', blank=True)  # Field name made lowercase.
    rfc = models.TextField(db_column='RFC', blank=True)  # Field name made lowercase.
    ddr = models.TextField(db_column='DDR', blank=True)  # Field name made lowercase.
    cader = models.TextField(db_column='CADER', blank=True)  # Field name made lowercase.
    municipio = models.TextField(db_column='MUNICIPIO', blank=True)  # Field name made lowercase.
    localidad = models.TextField(db_column='LOCALIDAD', blank=True)  # Field name made lowercase.
    beneficio = models.TextField(db_column='BENEFICIO', blank=True)  # Field name made lowercase.
    concepto = models.TextField(db_column='CONCEPTO', blank=True)  # Field name made lowercase.
    cantidad = models.TextField(db_column='CANTIDAD', blank=True)  # Field name made lowercase.
    precio_unitario = models.TextField(db_column='PRECIO UNITARIO', blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    inversion_total = models.TextField(db_column='INVERSION TOTAL', blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    apoyo_federal_dictaminado = models.TextField(db_column='APOYO FEDERAL DICTAMINADO', blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rfc_proovedor = models.TextField(db_column='RFC PROOVEDOR', blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    proveedor = models.TextField(db_column='PROVEEDOR', blank=True)  # Field name made lowercase.
    monto_autorizado = models.TextField(db_column='MONTO AUTORIZADO', blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    factura = models.TextField(db_column='FACTURA', blank=True)  # Field name made lowercase.
    fecha_factura = models.TextField(db_column='FECHA FACTURA', blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    clabe = models.TextField(db_column='CLABE', blank=True)  # Field name made lowercase.
    comprobante_sat = models.IntegerField(db_column='COMPROBANTE SAT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nombre_de_banco = models.TextField(db_column='NOMBRE DE BANCO', blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    solicitud = models.IntegerField(db_column='SOLICITUD', blank=True, null=True)  # Field name made lowercase.
    identif = models.IntegerField(db_column='IDENTIF', blank=True, null=True)  # Field name made lowercase.
    comprobante_curp = models.IntegerField(db_column='COMPROBANTE CURP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    comp_domic = models.IntegerField(db_column='COMP DOMIC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    carta_autoriz = models.IntegerField(db_column='CARTA AUTORIZ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cotizacion = models.IntegerField(db_column='COTIZACION', blank=True, null=True)  # Field name made lowercase.
    poder_en_su_caso = models.IntegerField(db_column='PODER EN SU CASO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fact = models.IntegerField(db_column='FACT', blank=True, null=True)  # Field name made lowercase.
    carta_pago_terceros = models.IntegerField(db_column='CARTA PAGO TERCEROS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reporte_verif = models.IntegerField(db_column='REPORTE VERIF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    carta_entrega_recepcion = models.IntegerField(db_column='CARTA ENTREGA-RECEPCION', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    certificado_parcelario = models.IntegerField(db_column='CERTIFICADO PARCELARIO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    oservaciones = models.IntegerField(db_column='OSERVACIONES', blank=True, null=True)  # Field name made lowercase.
    factura_del_tractor = models.IntegerField(db_column='FACTURA DEL TRACTOR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fotogarfias = models.IntegerField(db_column='FOTOGARFIAS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'solicitudes'
