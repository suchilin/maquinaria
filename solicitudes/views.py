from django.forms.models import modelformset_factory
from django.shortcuts import render, redirect
from solicitudes.models import Solicitudes
from .forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from datetime import date



def is_in_group(user_, group_):
    if user_:
        return user_.groups.filter(name=group_).count() > 0
    return False

@login_required
def index(request):
    SolicitudFormSet = modelformset_factory(Solicitudes, form =SolicitudForm)
    user_ = request.user
    if hasattr(user_, 'perfil') == False:
        return redirect(reverse('solicitudes:perfil'))
    if user_.username == 'jesus':
        query = Solicitudes.objects.all()
    else:
        query = Solicitudes.objects.filter(sol_status='SOLICITUD AUTORIZADA')
        if is_in_group(user_, 'proveedores'):
            query = query.filter(rfc_proovedor=user_.username)
    query = query.order_by('id')
    nombre = request.GET.get('nombre')
    identificador = request.GET.get('identificador')
    if(nombre):
        query = query.filter(nombre__icontains=nombre)
    if(identificador):
        query = query.filter(identificador=identificador)
    paginator = Paginator(query, 100) # Show 10 forms per page
    page = request.GET.get('page')
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)
    page_query = query.filter(id__in=[object.id for object in objects])
    lista = []
    formset = SolicitudFormSet(queryset=page_query)
    context = {'objects': objects, 'formset': formset, 'lista':lista}
    if request.method == 'POST':
        formset = SolicitudFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
    return render(request, 'solicitudes.html', context)

@login_required
def add(request):
    form = AddForm()
    if request.POST:
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/solicitudes/')
    return render(request, 'add.html', {'form': form})

@login_required
def perfil(request):
    try:
        uperfil = request.user.perfil
        form = PerfilForm(instance=uperfil)
    except:
        form = PerfilForm()
    if request.POST:
        form = PerfilForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('/idetec/solicitudes/')
    return render(request, 'perfil.html',{'form':form})

@login_required
def updateperfil(request):
    uperfil = request.user.perfil
    form = PerfilForm(instance=uperfil)
    if request.POST:
        form = PerfilForm(request.POST, instance=uperfil)
        if form.is_valid():
            form.save()
            return redirect(reverse('solicitudes:index'))
    return render(request, 'updateperfil.html',{'form':form})

@login_required
def ccdd(request, solicitud_id=None):
    solicitud = Solicitudes.objects.get(pk=solicitud_id)
    return render(request, 'ccdd.html', {'solicitud':solicitud})


@login_required
def centr(request, solicitud_id=None):
    solicitud = Solicitudes.objects.get(pk=solicitud_id)
    mes_ = {1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio", 7:"Julio", 8:"Agosto", 9:"Septiembre", 10:"Octubre", 11:"Noviembre", 12:"Diciembre"}
    fecha = date.today()
    dia = fecha.day
    mes = mes_[fecha.month]
    return render(request, 'centr.html', {'solicitud':solicitud, 'dia':dia, 'mes':mes})

@login_required
def update(request):
    solicitud_id=request.GET.get('solicitud_id')
    if solicitud_id:
        solicitud = Solicitudes.objects.get(id = solicitud_id)
        form = AddForm(instance=solicitud)
    if request.POST:
        solicitud_id=request.POST.get('id')
        solicitud = Solicitudes.objects.get(id = solicitud_id)
        form = AddForm(request.POST, instance=solicitud)
        if form.is_valid():
            form.save()
            return redirect('/idetec/solicitudes/')
    return render(request, 'update.html', {'form': form})

@login_required
def UnaSolicitud(request, solicitud_id = None):
    solicitud = Solicitudes.objects.get(id=solicitud_id)
    form = UnaSolicitudForm(instance=solicitud)
    return render(request, 'unasolicitud.html', {'form': form})
