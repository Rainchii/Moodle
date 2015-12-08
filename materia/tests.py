from django.test import TestCase
from Materia.models import Materia
from django.test import Client


# Create your tests here.

class ModelMateriaTest(TestCase):
	def test_string_str(self):
        mat = Materia(titulo="Materia")
        self.assertEqual(str(mat), mat.titulo)

    def test_verbose_name_no_plural(self):
        self.assertEqual(str(Materia._meta.verbose_name_plural), "materia")

class ViewMateriaTest(TestCase):

	def test_view_basico(self):
        response = self.c.get(self.materia.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_titulo_materia(self):
        response = self.c.get(self.materia.get_absolute_url())
        self.assertContains(response, self.materia.titulo)

    def test_no_hay_materias(self):
        response = self.c.get('/Materia/')
        self.assertContains(response, 'Sin materias')