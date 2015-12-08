Feature: Como administrador del sistema
		quiero agregar examenes
		para realizar evaluaciones a los alumnos registrados.

Scenario: Verificar la instalacion de la app
	Given que ingrese al panel de administracion
	When se muestra la pantalla de bienvenida
	Then Puedo ver en pantalla la opcion "Examen".

Scenario: Verificar que se muestra el formulario
	Given que ingrese al panel de administracion
	When doy click en la opcion Examen y despues en la opcion "Agregar examen"
	Then puedo ver en pantalla "11" cajas de texto.

Scenario: Verificar la creacion del examen
	Given que ingrese al panel de administracion 
	When ingreso a "http://localhost:8000/admin/Examen/examen/add/" lleno los datos necesarios y presiono el boton "Guardar"
	Then se muestra un mensaje con el texto "Se agregó con éxito".