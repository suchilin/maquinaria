from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import csv
from django.shortcuts import render
from solicitudes.models import Solicitudes
import xlrd
from django.contrib.admin.views.decorators import staff_member_required
import unicodedata


def remove_accents(input_str):
    nkfd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nkfd_form.encode('ASCII', 'ignore')
    return only_ascii

class Command(BaseCommand):
    help = 'Importing data to database'

    #def add_arguments(self, parser):
        #parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        filename = 'files/db.xlsx'
        workbook = xlrd.open_workbook(filename)
        first_sheet = workbook.sheet_by_index(0)
        print 'init task...'
        sols = []
        for i in range(1, first_sheet.nrows):
            row = first_sheet.row(i)
            # print row[1].value
            solicitudes = Solicitudes.objects.filter(folio = row[2].value)
            try:
                solicitud = solicitudes[0]
            except:
                solicitud = Solicitudes()
            solicitud.delegacion = row[0].value
            solicitud.curp = row[10].value
            solicitud.folio = row[1].value
            solicitud.nombre = row[7].value + ' ' + row[8].value + ' '+row[9].value
            solicitud.rfc = row[11].value
            solicitud.ddr = row[19].value
            if isinstance(row[20].value, unicode):
                solicitud.cader = remove_accents(row[20].value)
            else:
                solicitud.cader = row[20].value
            solicitud.municipio = row[23].value
            solicitud.localidad = row[24].value
            solicitud.beneficio = row[32].value
            solicitud.concepto = row[35].value
            try:
                solicitud.cantidad = float(row[39].value)
            except:
                pass
            try:
                solicitud.precio_unitario = float(row[40].value)
            except:
                pass
            try:
                solicitud.inversion_total = float(row[41].value)
            except:
                pass
            try:
                solicitud.apoyo_federal_dictaminado = float(row[54].value)
            except:
                pass
            solicitud.marca = row[103].value
            solicitud.modelo = row[104].value
            solicitud.rfc_proovedor = row[105].value
            solicitud.proveedor = row[106].value
            try:
                solicitud.monto_autorizado = float(row[62].value)
            except:
                pass
            solicitud.sol_status = row[108].value
            sols.append(solicitud)
            rows = i
            print i, " ", solicitud.folio
        Solicitudes.objects.bulk_create(sols)
        print "End Task!"

