from django import forms
from .models import Examen


class ExamenForm(forms.ModelForm):

    class Meta(object):
        model = Examen
        fields = ['titulo', 'pregunta1', 'respuesta1',
            'pregunta2', 'respuesta2', 'pregunta3', 'respuesta3',
            'pregunta4', 'respuesta4', 'pregunta5', 'respuesta5']


class ContestarExamenForm(forms.ModelForm):

    class Meta(object):
        model = Examen
        fields = ['respuesta1', 'respuesta2', 'respuesta3',
            'respuesta4', 'respuesta5']
