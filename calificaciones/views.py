from django.shortcuts import render, redirect
from calificaciones.forms import CalificacionForm
from django.contrib.auth.models import Group, User


# Create your views here.
#@permission_required('usuarios.can_add','index')
def nueva(request):
    usuario = User.objects.all()
    form = CalificacionForm({'calificacion': '10'}, alumno=usuario)
    print (form.is_valid())
    if form.is_valid():
        user = form.save()
        user.save()
    return redirect('/alumnos/')
    #else:
