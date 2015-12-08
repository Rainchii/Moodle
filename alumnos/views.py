# coding: utf-8
from django.shortcuts import render,redirect, get_object_or_404
from alumnos.models import Alumno
from alumnos.forms import AlumnoForm
from calificaciones.models import Calificacion
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import Group, User
from django.contrib.auth.hashers import make_password
# Create your views here.
@login_required
def index_view(request):
	alumnos = User.objects.all()
	return render(request, 'alumnos/principal.html', {'alumnos': alumnos})

def login_view(request):
    # Si el usuario esta ya logueado, lo redireccionamos a index_view
    if request.user.is_authenticated():
       return render(request, 'alumnos/principal.html', {})

    mensaje = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print user
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'alumnos/principal.html', {'mensaje': mensaje})
            else:
                # Redireccionar informando que la cuenta esta inactiva
                # Lo dejo como ejercicio al lector :)
				return render(request, 'alumnos/principal.html', {'mensaje': mensaje})
        else:
            mensaje = 'Nombre de usuario o contraseña no válido'
    return render(request, 'alumnos/login.html', {'mensaje': mensaje})

def cerrar(request):
    logout(request)
    return redirect('login_view')

def nuevoA(request):

    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            al = form.save()
            al.save()
            al.is_staff = True
            g = Group.objects.get(name='GroupAlum') 
            g.user_set.add(al)
            return redirect('alumnos.views.login_view')
    else:
        form = AlumnoForm
    return render (request,'alumnos/nuevoAlumno.html',{'form':form, 'etiqueta':'Nuevo'})

def listar(request):
	alumno = User.objects.all()
	return render(request, 'alumnos/lista.html', {'alumnos' : alumno})


def editar_post(request):
	if request.POST.get('idEditar'):
		alumno = User.objects.get(id = request.POST.get('idEditar'))
		form = AlumnoForm(instance=alumno)
		
	else:
		alumno = User.objects.get(id = request.POST.get('id'))
		form = AlumnoForm(request.POST, instance=alumno)
		if form.is_valid():
			alumno = form.save()
			alumno.save()
			return redirect('alumnos/listar')

	return render(request, 'alumnos/nuevoAlumno.html', {'form':form, 'id' : alumno.id, 'etiqueta': 'Actualizar'})


def consultar_calificaciones(request):
    try:
        calificaciones = Calificacion.objects.all()
        s = []
        for calificacion in calificaciones:
            if int(calificacion.alumno_id) == int(request.POST.get('idCalificacion')):
            	print ('si entro')
                s.append(calificacion)

    except Calificacion.DoesNotExist:
        calificaciones = []
    return render(request, 'alumnos/calificaciones.html', {'calificaciones' : s})
