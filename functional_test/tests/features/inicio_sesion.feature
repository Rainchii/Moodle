Feature: Como alumno
  Quiero loggearme en el sistema
  para que entrar a mi sesion y 
  trabajar en ella

  Scenario: Entrar en el sistema como alumno Sari
	Given Que ingreso el texto "sari" en el campo de Username, el texto "hola" en el campo de password
	Cuando Oprimo el boton de iniciarSesion
	Entonces Puedo ver el titulo de "Bienvenido al Moodle" en la pantalla

  Scenario: Entrar en el sistema como alumno Sari
	Given Que ingreso el texto "moodle" en el campo de Username, el texto "moodle" en el campo de password
	Cuando Oprimo el boton de iniciarSesion
	Entonces Puedo ver el titulo de "Bienvenido al Moodle" en la pantalla

  Scenario: Entrar en el sistema como alumno Sari
	Given Que ingreso el texto "sam" en el campo de Username, el texto "sam" en el campo de password
	Cuando Oprimo el boton de iniciarSesion
	Entonces Puedo ver el titulo de "Bienvenido al Moodle" en la pantalla
