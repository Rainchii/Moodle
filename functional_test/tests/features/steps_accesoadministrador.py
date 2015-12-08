# -*- coding: utf-8 -*-
from lettuce import step, world
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


@step(u'Given Ingresar en el navegador la url "([^"]*)" en la barra de direcciones')
def given_ingresar_en_el_navegador_la_url_group1_en_la_barra_de_direcciones(step, urlDjango):
	world.driver = webdriver.Firefox()
	world.driver.get(urlDjango)


@step(u'When Introduzco el texto "([^"]*)" en el campo Username, el texto "([^"]*)" en el campo Password y oprimo la tecla Enter')
def when_introduzco_el_texto_group1_en_el_campo_username_el_texto_group1_en_el_campo_password_y_oprimo_la_tecla_enter(step, usernname, password):
	user = world.driver.find_element_by_id('id_username')
	user.send_keys(usernname)
	passw = world.driver.find_element_by_id('id_password')
	passw.send_keys(password)
	passw.send_keys(Keys.RETURN)


@step(u'Then Puedo ver en el titulo del navegador la palabra "([^"]*)".')
def then_puedo_ver_en_el_titulo_del_navegador_la_palabra_group1(step, browserTitle):
    assert browserTitle in world.driver.title