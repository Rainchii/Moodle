# coding: utf-8
from django import forms
from calificaciones.models import Calificacion


class CalificacionForm(forms.ModelForm):
    """Formulario para dar servicio al modelo Calificacion"""
    #password = forms.CharField(widget=forms.PasswordInput, label=u'Contraseña')
    # idH = forms.IntegerField(widget=forms.HiddenInput)

    class Meta(object):
        model = Calificacion
        fields = ['calificacion', 'alumno']
