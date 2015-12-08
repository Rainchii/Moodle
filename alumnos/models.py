from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Alumno(models.Model):

	username = models.CharField(max_length=25)
	password = models.CharField(max_length=25)
	first_name = models.CharField(max_length=25)
	last_name = models.CharField('Apellidos',max_length=125)
	email = models.EmailField('E-mail', max_length=60)

	def __unicode__(self):
		return self.first_name + " " + self.last_name

