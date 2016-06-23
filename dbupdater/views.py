from django.shortcuts import render
from solicitudes.models import Solicitudes
from .forms import dbupdaterForm
import xlrd
from django.contrib.admin.views.decorators import staff_member_required
import unicodedata


def remove_accents(input_str):
    nkfd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nkfd_form.encode('ASCII', 'ignore')
    return only_ascii


@staff_member_required
def index(request):
    form = dbupdaterForm()
    if request.POST:
        form = dbupdaterForm(request.POST, request.FILES)
        if form.is_valid():
            filename = request.FILES['ExcelFile']
            workbook = xlrd.open_workbook(file_contents = filename.read())
            first_sheet = workbook.sheet_by_index(0)
            for i in range(1, first_sheet.nrows):
                row = first_sheet.row(i)
                if row[2]!="":
                    solicitudes = Solicitudes.objects.filter(folio = row[2].value)
                    try:
                        solicitud = solicitudes[0]
                    except:
                        continue
                        #solicitud = Solicitudes()
                    solicitud.delegacion = row[0].value
                    solicitud.curp = row[10].value
                    solicitud.folio = row[2].value
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
                    solicitud.concepto = row[34].value
                    solicitud.cantidad = float(row[39].value)
                    solicitud.precio_unitario = row[40].value
                    solicitud.inversion_total = row[41].value
                    solicitud.apoyo_federal_dictaminado = row[54].value
                    solicitud.marca = row[96].value
                    solicitud.modelo = row[97].value
                    solicitud.rfc_proovedor = row[98].value
                    solicitud.proveedor = row[99].value
                    solicitud.monto_autorizado = row[62].value
                    solicitud.sol_status = row[101].value
                    solicitud.save()
                    rows = i
            context = {'form':form, 'name':filename, 'rows':rows }
            return render(request, 'dbupdater/index.html', context )
    return render(request, 'dbupdater/index.html', {'form':form})
