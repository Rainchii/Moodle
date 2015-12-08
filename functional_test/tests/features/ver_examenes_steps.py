# -*- coding: utf-8 -*-
from lettuce import step, world
from selenium import webdriver
from nose.tools import assert_equals


@step(u'Given inicio sesion en el sistema y se me muestra la pantalla principal')
def given_inicio_sesion_en_el_sistema_y_se_me_muestra_la_pantalla_principal(step):
    world.driver = webdriver.Firefox()
    world.driver.get("localhost:8000/Examen/")


@step(u'When doy clic en la opcion "([^"]*)"')
def when_doy_clic_en_la_opcion_ver_examenes(step, opcion):
    world.driver.get("localhost:8000/Examen/")


@step(u'Then Puedo ver en pantalla el titulo "([^"]*)".')
def then_puedo_ver_en_pantalla_el_titulo_ver_examen(step, titulo):
    title = world.driver.find_element_by_id("titulo")
    world.driver.close()
    assert titulo in title.text


# Scenario 2
@step(u'Then Puedo ver en pantalla una lista de examenes.')
def then_puedo_ver_en_pantalla_una_lista_de_examenes(step):
    examenes = world.driver.find_elements_by_css_selector('h4')
    world.driver.close()
    assert len(examenes) > 0

# Scenario 3
@step(u'Given ingrese a la direccion "([^"]*)"')
def given_ingrese_a_la_direccion_direccion(step, direccion):
    world.driver = webdriver.Firefox()
    world.driver.get(direccion)


@step(u'When doy clic en algun examen creado')
def when_doy_clic_en_algun_examen_creado(step):
    clic = world.driver.find_element_by_xpath("//*[@type='submit']")
    clic.click()


@step(u'Then Puedo ver en pantalla un formulario con "([^"]*)" cajas de texto.')
def then_puedo_ver_en_pantalla_un_formulario_con_group1_cajas_de_texto(step, cantC):
    examenes = world.driver.find_elements_by_xpath('//*[@type="text"]')
    print ("holaaaaa")
    world.driver.close()
    assert len(examenes) <= cantC
