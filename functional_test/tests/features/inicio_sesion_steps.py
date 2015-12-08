# -*- coding: utf-8 -*-
from lettuce import step, world
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

@step(u'Given Que ingreso el texto "([^"]*)" en el campo de Username, el texto "([^"]*)" en el campo de password')
def given_que_ingreso_el_texto_group1_en_el_campo_de_username_el_texto_group2_en_el_campo_de_password(step, group1, group2):
    world.driver = webdriver.Firefox()
    world.driver.get("http://10.1.39.174:9000/alumnos")
    user = world.driver.find_element_by_id("username")
    user.send_keys(group1)
    password = world.driver.find_element_by_id("password")
    password.send_keys(group2)

@step(u'Cuando Oprimo el boton de iniciarSesion')
def cuando_oprimo_el_boton_de_iniciarsesion(step):
    click = world.driver.find_element_by_id("btnLogin")
    click.click()
    time.sleep(3)

@step(u'Entonces Puedo ver el titulo de "([^"]*)" en la pantalla')
def entonces_puedo_ver_el_titulo_de_group1_en_la_pantalla(step, group1):
    assert group1 in world.driver.title
