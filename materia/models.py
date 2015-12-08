from django.db import models

# Create your models here.
class Materia(models.Model):

	nombre = models.CharField(max_length=25)
	ciclo = models.CharField(max_length=25)
	grupo = models.CharField(max_length=125)
	capacidad = models.IntegerField(default=0)

	def __unicode__(self):
		return self.nombre 