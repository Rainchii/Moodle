from django.conf.urls import url
from Examen.views import ver_examenes, contestar_examen, revisar_examen


urlpatterns = [
    url(r'^$', ver_examenes, name='examenes'),
    url(r'^contestar_examen', contestar_examen, name='contestarEx'),
    url(r'^revisar_examen', revisar_examen, name='revisar'),
]
