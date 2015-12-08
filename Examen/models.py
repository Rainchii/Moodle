from django.db import models


# Create your models here.
class Examen(models.Model):
    class Meta:
        verbose_name_plural = "examen"

    titulo = models.CharField(max_length=120)
    pregunta1 = models.CharField(max_length=120)
    respuesta1 = models.CharField(max_length=120)
    pregunta2 = models.CharField(max_length=120)
    respuesta2 = models.CharField(max_length=120)
    pregunta3 = models.CharField(max_length=120)
    respuesta3 = models.CharField(max_length=120)
    pregunta4 = models.CharField(max_length=120)
    respuesta4 = models.CharField(max_length=120)
    pregunta5 = models.CharField(max_length=120)
    respuesta5 = models.CharField(max_length=120)

    def get_absolute_url(self):
        return "/Examen/"
    # uso de toString en python

    def __unicode__(self):
        return self.titulo
