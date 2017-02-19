from django import forms
from .models import *


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ('__all__')


    def __init__(self, *args, **kwargs):
        super(EventoForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})

        self.fields['inicio'].widget.attrs.update({'class':'form-control datetime'})
        self.fields['termino'].widget.attrs.update({'class':'form-control datetime'})