from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import csv
from django.shortcuts import render
from solicitudes15.models import Solicitudes
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
        filename = 'files/db_facturas.xlsx'
        workbook = xlrd.open_workbook(filename)
        first_sheet = workbook.sheet_by_index(0)
        for i in range(1, first_sheet.nrows):
            row = first_sheet.row(i)
            if row[1]!="" and row[21]='PAGADO':
                solicitudes = Solicitudes.objects.filter(folio = row[1].value)
                try:
                    solicitud = solicitudes[0]
                except:
                    continue
                solicitud.factura = row[25].value.replace(' ','')
                solicitud.save()
                rows = i
            print i, " ", solicitud.folio
        print "End Task!"

