# -*- coding: utf-8 -*-
from lettuce import step, world
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

@step(u'Given Que ingreso la materia "([^"]*)" en la caja de texto')
def given_que_ingreso_la_materia_pruebas_en_la_caja_de_texto(step, group1):
    world.driver = webdriver.Firefox()
    world.driver.get("http://10.1.39.174:9000/admin/login/?next=/admin/")
    user = world.driver.find_element_by_id("id_username")
    user.send_keys("moodle")
    password = world.driver.find_element_by_id("id_password")
    password.send_keys("moodle")
    click = world.driver.find_element_by_xpath("//*[@type='submit']")
    click.click()
    clickAddMateria = world.driver.find_element_by_css_selector("[href*='/admin/materia/materia/add/']")
    clickAddMateria.click()
    time.sleep(3)
    nombre = world.driver.find_element_by_id("id_nombre")
    nombre.send_keys(group1)
    ciclo = world.driver.find_element_by_id("id_ciclo")
    ciclo.send_keys("2015-2016")
    grupo = world.driver.find_element_by_id("id_grupo")
    grupo.send_keys("7B")
    capacidad = world.driver.find_element_by_id("id_capacidad")
    capacidad.send_keys(30)
    time.sleep(3)


@step(u'Cuando Oprimo el boton de guardar')
def cuando_oprimo_el_boton_de_guardar(step):
    btnSave = world.driver.find_element_by_name("_save")
    btnSave.click()


@step(u'Entonces Puedo ver la alerta de "([^"]*)" en la pantalla')
def entonces_puedo_ver_la_alerta_de_group1_en_la_pantalla(step, group1):
    materia = world.driver.find_element_by_class_name('success')