from django.db import models
from django.contrib.auth.models import Group, User


# Create your models here.
class Calificacion(models.Model):
	calificacion = models.CharField(max_length=25)
	alumno = models.ForeignKey(User)

	def __unicode__(self):
		return self.calificacion
