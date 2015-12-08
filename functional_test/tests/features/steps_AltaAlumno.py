# -*- coding: utf-8 -*-
from lettuce import step, world
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@step(u'Given Ingresar en el navegador la url "([^"]*)" en la barra de direcciones')
def given_ingresar_en_el_navegador_la_url_group1_en_la_barra_de_direcciones(step, urlDjango):
	world.driver = webdriver.Firefox()
	world.driver.get(urlDjango)


@step(u'When Introduzca el texto "([^"]*)" en el campo Username, el texto "([^"]*)" en el campo contraseña, el texto "([^"]*)" en el campo Nombre, el texto "([^"]*)" en el campo Apellidos, el texto "([^"]*)" en el campo E-mail y oprimo la tecla Enter')
def when_introduzca_el_texto_group1_en_el_campo_username_el_texto_group2_en_el_campo_contrasena_el_texto_group3_en_el_campo_nombre_el_texto_group4_en_el_campo_apellidos_el_texto_group5_en_el_campo_e_mail_y_oprimo_la_tecla_enter(step, username, password, nombre, apellidos, email):
	user = world.driver.find_element_by_id('id_username')
	user.send_keys(username)
	passw = world.driver.find_element_by_id('id_password')
	passw.send_keys(password)
	nom = world.driver.find_element_by_id('id_nombre')
	nom.send_keys(nombre)
	ape = world.driver.find_element_by_id('id_apellidos')
	ape.send_keys(apellidos)
	mail = world.driver.find_element_by_id('id_mail')
	mail.send_keys(email)
	passw.send_keys(Keys.RETURN)


@step(u'Then Puedo ver en el titulo del navegador la palabra "([^"]*)".')
def then_puedo_ver_en_el_titulo_del_navegador_la_palabra_group1(step, browserTitle):
    assert browserTitle in world.driver.title
