from django import forms


class dbupdaterForm(forms.Form):
    ExcelFile = forms.FileField()
