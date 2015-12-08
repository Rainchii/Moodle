from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Examen
from .forms import ContestarExamenForm


def ver_examenes(request):
    # hacer prueba
    examenes = Examen.objects.all()
    title = ""
    if(len(examenes) > 0):
        title = "Examenes Disponibles"
    else:
        title = "No hay examenes"
    return render(request, 'Examen/ver_examenes.html',
                  {'examenes': examenes, 'title': title})


def revisar_examen(request):
    calificacion = 0
    if request.method == "POST":
        form = ContestarExamenForm(request.POST)
        if form.is_valid():
            examenC = Examen.objects.get(id=request.POST.get('id'))
            examenN = form.save(commit=False)
            if(examenC.respuesta1 == examenN.respuesta1):
                calificacion += 20
            if(examenC.respuesta2 == examenN.respuesta2):
                calificacion += 20
            if(examenC.respuesta3 == examenN.respuesta3):
                calificacion += 20
            if(examenC.respuesta4 == examenN.respuesta4):
                calificacion += 20
            if(examenC.respuesta5 == examenN.respuesta5):
                calificacion += 20
            request.session['cal'] = calificacion
            return HttpResponseRedirect('/calificaciones/nueva/')
        else:
            return redirect('examenes')
    return redirect('examenes')


def contestar_examen(request):
    examen = None
    if request.POST.get('id'):
        examen = Examen.objects.get(id=request.POST.get('id'))
        form = ContestarExamenForm()
        form.fields['respuesta1'].label = examen.pregunta1
        form.fields['respuesta2'].label = examen.pregunta2
        form.fields['respuesta3'].label = examen.pregunta3
        form.fields['respuesta4'].label = examen.pregunta4
        form.fields['respuesta5'].label = examen.pregunta5
    return render(request, 'Examen/contestar_examen.html',
                  {'form': form, 'id': examen.id, 'titulo': examen.titulo})
