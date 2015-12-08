#coding: utf-8
from django import forms 
from materia.models import Materia

class MateriaForm(forms.ModelForm):
	"""Formulario para dar servicio al modelo Materia"""
	

	class Meta(object):
		#clase que muestra que campos del modelo se muestren en el formulario
		model = Materia #siempre se debe llamar model
		fields = ['nombre', 'ciclo',  'grupo', 'capacidad']
