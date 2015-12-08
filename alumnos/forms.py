#coding: utf-8
from django import forms 
from alumnos.models import Alumno
from django.contrib.auth.models import User

class AlumnoForm(forms.ModelForm):
	"""Formulario para dar servicio al modelo Usuario"""
	password = forms.CharField(widget=forms.PasswordInput, label =u'Contraseña')
	

	class Meta(object):
		#clase que muestra que campos del modelo se muestren en el formulario
		model = User #siempre se debe llamar model
		fields = ['username', 'password', 'first_name', 'last_name','email']