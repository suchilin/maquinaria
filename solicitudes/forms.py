from django.forms import ModelForm
from .models import Solicitudes, ProvProfile
from django import forms

class SolicitudForm(ModelForm):
    class Meta:
        model = Solicitudes
        fields = ['id','identificador','nombre','folio','apoyo_federal_dictaminado','beneficio',
                'fact', 'carta_pago_terceros', 'reporte_verif',
                  'carta_entrega_recepcion', 'oservaciones',
                  'sol_status']
        widgets = {
                        'beneficio': forms.HiddenInput(),
                        'nombre': forms.HiddenInput(),
                        'folio': forms.HiddenInput(),
                        'oservaciones': forms.Textarea(attrs={'rows':1, 'cols':15}),
                        'id': forms.HiddenInput(),
                        'apoyo_federal_dictaminado': forms.HiddenInput(),
                        'identificador': forms.HiddenInput(),
                  }

class UnaSolicitudForm(ModelForm):
    class Meta:
        model = Solicitudes
        widgets = {
                        'id': forms.HiddenInput(),
        }



class AddForm(ModelForm):
    class Meta:
        model = Solicitudes
        fields = ['id','identificador','nombre','folio','apoyo_federal_dictaminado','beneficio',
                'fact', 'carta_pago_terceros', 'reporte_verif',
                  'carta_entrega_recepcion', 'oservaciones',
                  'sol_status']
        widgets = {
                        'id': forms.HiddenInput(),
                        'cader': forms.HiddenInput(),
                        'nombre': forms.Textarea(attrs={'rows':1, 'cols':15}),
                        'folio': forms.Textarea(attrs={'rows':1, 'cols':15}),
                        'oservaciones': forms.Textarea(attrs={'rows':1, 'cols':15}),
                  }


class PerfilForm(ModelForm):
    class Meta:
        model = ProvProfile
        exclude=['user',]
