from django.test import TestCase
from Examen.models import Examen
from Examen.forms import ExamenForm, ContestarExamenForm
from django.test import Client


class ModelExamenTest(TestCase):

    def test_string_str(self):
        ex = Examen(titulo="Math")
        self.assertEqual(str(ex), ex.titulo)

    def test_verbose_name_no_plural(self):
        self.assertEqual(str(Examen._meta.verbose_name_plural), "examen")


class ViewExamenTest(TestCase):

    def setUp(self):
        self.c = Client()
        self.examen = Examen.objects.create(titulo='ex-1',
                                            pregunta1='p1', respuesta1='r1',
                                            pregunta2='p2', respuesta2='r2',
                                            pregunta3='p3', respuesta3='r3',
                                            pregunta4='p4', respuesta4='r4',
                                            pregunta5='p5', respuesta5='r5')

    def test_view_basico(self):
        response = self.c.get(self.examen.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_titulo_del_examen(self):
        response = self.c.get(self.examen.get_absolute_url())
        self.assertContains(response, self.examen.titulo)


class ExamenFormTest(TestCase):

    def setUp(self):
        self.examen = Examen.objects.create(titulo='ex-1',
                                            pregunta1='p1', respuesta1='r1',
                                            pregunta2='p2', respuesta2='r2',
                                            pregunta3='p3', respuesta3='r3',
                                            pregunta4='p4', respuesta4='r4',
                                            pregunta5='p5', respuesta5='r5')

    def test_init(self):
        ExamenForm(self.examen)

    def test_valid_data(self):
        form = ExamenForm({
                          'titulo': 'ex-1',
                          'pregunta1': 'p1',
                          'respuesta1': 'r1',
                          'pregunta2': 'p2',
                          'respuesta2': 'r2',
                          'pregunta3': 'p3',
                          'respuesta3': 'r3',
                          'pregunta4': 'p4',
                          'respuesta4': 'r4',
                          'pregunta5': 'p5',
                          'respuesta5': 'r5'
                          })
        self.assertTrue(form.is_valid())
        ex = form.save()
        self.assertEqual(ex.titulo, "ex-1")
        self.assertEqual(ex.pregunta1, "p1")
        self.assertEqual(ex.respuesta1, "r1")
        self.assertEqual(ex.pregunta2, "p2")
        self.assertEqual(ex.respuesta2, "r2")
        self.assertEqual(ex.pregunta3, "p3")
        self.assertEqual(ex.respuesta3, "r3")
        self.assertEqual(ex.pregunta4, "p4")
        self.assertEqual(ex.respuesta4, "r4")
        self.assertEqual(ex.pregunta5, "p5")
        self.assertEqual(ex.respuesta5, "r5")

    def test_calificar_examen(self):
        form = ExamenForm({
                          'titulo': 'ex-1',
                          'pregunta1': 'p1',
                          'respuesta1': 'r1',
                          'pregunta2': 'p2',
                          'respuesta2': 'r2',
                          'pregunta3': 'p3',
                          'respuesta3': 'r3',
                          'pregunta4': 'p4',
                          'respuesta4': 'r4',
                          'pregunta5': 'p5',
                          'respuesta5': 'r5'
                          })
        self.assertTrue(form.is_valid())
        ex = form.save()
        self.assertEqual(ex.titulo, "ex-1")
        self.assertEqual(ex.pregunta1, "p1")
        self.assertEqual(ex.respuesta1, "r1")
        self.assertEqual(ex.pregunta2, "p2")
        self.assertEqual(ex.respuesta2, "r2")
        self.assertEqual(ex.pregunta3, "p3")
        self.assertEqual(ex.respuesta3, "r3")
        self.assertEqual(ex.pregunta4, "p4")
        self.assertEqual(ex.respuesta4, "r4")
        self.assertEqual(ex.pregunta5, "p5")
        self.assertEqual(ex.respuesta5, "r5")
        form = ContestarExamenForm({
                                   'respuesta1': 'r1',
                                   'respuesta2': 'r2',
                                   'respuesta3': 'r3',
                                   'respuesta4': 'r4',
                                   'respuesta5': 'r5'
                                   })
        self.assertTrue(form.is_valid())
        exCont = form.save(commit=False)
        self.assertEqual(exCont.respuesta1, ex.respuesta1)
        self.assertEqual(exCont.respuesta2, ex.respuesta2)
        self.assertEqual(exCont.respuesta3, ex.respuesta3)
        self.assertEqual(exCont.respuesta4, ex.respuesta4)
        self.assertEqual(exCont.respuesta5, ex.respuesta5)


class TestExamenes(TestCase):

    def setUp(self):
        self.c = Client()

    def test_url_examen_root(self):
        response = self.c.get('/Examen/')
        self.assertEqual(response.status_code, 200)

    def test_registro_de_un_examen(self):
        Examen.objects.create(titulo='ex-1',
                              pregunta1='p1', respuesta1='r1',
                              pregunta2='p2', respuesta2='r2',
                              pregunta3='p3', respuesta3='r3',
                              pregunta4='p4', respuesta4='r4',
                              pregunta5='p5', respuesta5='r5')
        response = self.c.get('/Examen/')
        self.assertContains(response, 'ex-1')

    def test_no_hay_examenes(self):
        response = self.c.get('/Examen/')
        self.assertContains(response, 'No hay examenes')
