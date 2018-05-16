from django import forms
from django.forms import ModelForm
from .models import *

class AddGagetForm(ModelForm):
    class Meta:
        model = tb_Gaget
        fields = ('Tipo', 'Modelo', 'Fabricante', 'Slope', 'Offset', 'Serial', 'Calibracao')

    def __init__(self, *args, **kwargs):
        super(AddGagetForm, self).__init__(*args, **kwargs)
        self.fields['Tipo'].widget.attrs['class']="form-control"
        self.fields['Modelo'].widget.attrs['class'] = "form-control"
        self.fields['Fabricante'].widget.attrs['class'] = "form-control"
        self.fields['Slope'].widget.attrs['class'] = "form-control"
        self.fields['Offset'].widget.attrs['class'] = "form-control"
        self.fields['Serial'].widget.attrs['class'] = "form-control"
        self.fields['Calibracao'].widget.attrs['class'] = "form-control"
