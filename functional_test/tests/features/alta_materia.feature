Feature: Como docente
  Quiero registrar materias
  para que los alumnos puedan 
  trabajar en ellas

  Scenario: Dar de alta la materia Pruebas
	Given Que ingreso la materia "Pruebas" en la caja de texto
	Cuando Oprimo el boton de guardar
	Entonces Puedo ver la alerta de "success" en la pantalla

  Scenario: Dar de alta la materia Videojuegos
	Given Que ingreso la materia "Videojuegos" en la caja de texto
	Cuando Oprimo el boton de guardar
	Entonces Puedo ver la alerta de "success" en la pantalla

  Scenario: Dar de alta la materia Seguridad
	Given Que ingreso la materia "Seguridad" en la caja de texto
	Cuando Oprimo el boton de guardar
	Entonces Puedo ver la alerta de "success" en la pantalla