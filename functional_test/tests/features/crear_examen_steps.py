# -*- coding: utf-8 -*-
from lettuce import step, world
from selenium import webdriver
from nose.tools import assert_equals


# scenario 1
@step(u'Given que ingrese al panel de administracion')
def given_que_ingrese_al_panel_de_administracion(step):
    world.driver = webdriver.Firefox()
    world.driver.get("localhost:8000/admin")
    user = world.driver.find_element_by_id("id_username")
    user.send_keys("admin")
    password = world.driver.find_element_by_id("id_password")
    password.send_keys("admin")
    click = world.driver.find_element_by_xpath("//*[@type='submit']")
    click.click()


@step(u'When se muestra la pantalla de bienvenida')
def when_se_muestra_la_pantalla_de_bienvenida(step):
    browserTitle = u'Administración del sitio'
    assert browserTitle in world.driver.title


@step(u'Then Puedo ver en pantalla la opcion "([^"]*)".')
def then_puedo_ver_en_pantalla_la_opcion_examen(step, app):
    body = world.driver.find_element_by_tag_name('body')
    world.driver.close()
    assert app in body.text


# scenario 2
@step(u'When doy click en la opcion examen y despues en la opcion "([^"]*)"')
def when_doy_click_en_la_opcion_examen_y_despues_en_la_opcion_add_examen(step, addExamen):
    click = world.driver.find_element_by_xpath("//*[@href='/admin/Examen/examen/']")
    click.click()
    add = world.driver.find_element_by_xpath(
        "//*[@href='/admin/Examen/examen/add/']"
    )
    add.click()


@step(u'Then puedo ver en pantalla "([^"]*)" cajas de texto.')
def then_puedo_ver_en_pantalla_11_cajas_de_texto(step, cantCajas):
    count = world.driver.find_elements_by_xpath("//*[@type='text']")
    world.driver.close()
    #assert len(count) == cantCajas
    assert_equals(len(count), int(cantCajas))


# scenario 3
@step(u'When ingreso a "([^"]*)" lleno los datos necesarios y presiono el boton "([^"]*)"')
def when_ingreso_a_agregar_examen_lleno_los_datos_necesarios_y_presiono_el_boton_guardar(step, dirAgregar, btnGuardar):
    world.driver.get(dirAgregar)
    world.driver.find_element_by_name('titulo').send_keys("Examen Matematicas")
    world.driver.find_element_by_name('pregunta1').send_keys("pregunta 1")
    world.driver.find_element_by_name('respuesta1').send_keys("respuesta1")
    world.driver.find_element_by_name('pregunta2').send_keys("pregunta 2")
    world.driver.find_element_by_name('respuesta2').send_keys("respuesta2")
    world.driver.find_element_by_name('pregunta3').send_keys("pregunta 3")
    world.driver.find_element_by_name('respuesta3').send_keys("respuesta3")
    world.driver.find_element_by_name('pregunta4').send_keys("pregunta 4")
    world.driver.find_element_by_name('respuesta4').send_keys("respuesta4")
    world.driver.find_element_by_name('pregunta5').send_keys("pregunta 5")
    world.driver.find_element_by_name('respuesta5').send_keys("respuesta5")
    click = world.driver.find_element_by_xpath("//*[@name='_save']")
    click.click()


@step(u'Then se muestra un mensaje con el texto "([^"]*)"')
def then_se_muestra_un_mensaje_con_el_texto_mensaje(step, mensaje):
    body = world.driver.find_element_by_tag_name('body')
    assert mensaje in body.text
