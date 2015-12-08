from django.conf.urls import include, url
from .views import index_view, login_view, cerrar,nuevoA,listar,editar_post, consultar_calificaciones
#from Examen.views import ver_examenes


urlpatterns = [
    url(r'^$', login_view, name="login_view"),
    url(r'^index_view/$', index_view, name="index_view"),
    url(r'^cerrar/$', cerrar,  name="cerrar"),
    url(r'^nuevoA/$', nuevoA, name="nuevoA"),
    url(r'^listar/$', listar, name = 'listar'),
    url(r'^editar/$', editar_post, name="editar"),
    url(r'^calificacion/$', consultar_calificaciones, name="calificacion"),
    #url(r'^Examen/ver_examenes', ver_examenes, name="examenes"),
]
