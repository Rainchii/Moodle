Feature: Como alumno registrado en el sistema
		quiero poder ver los examenes disponibles
		para poder contestar aquellos que me interesen.

Scenario: Verificar que se muestre una la pagina de examenes
	Given inicio sesion en el sistema y se me muestra la pantalla principal
	When doy clic en la opcion "Ver examenes"
	Then Puedo ver en pantalla el titulo "Examenes Disponibles".

Scenario: Verificar que se muestre una lista de examenes
	Given inicio sesion en el sistema y se me muestra la pantalla principal
	When doy clic en la opcion "Ver examenes"
	Then Puedo ver en pantalla una lista de examenes.

Scenario: Verificar que muestra un formulario para contestar examen
	Given ingrese a la direccion "http://localhost:8000/Examen/"
	When doy clic en algun examen creado
	Then Puedo ver en pantalla un formulario con "5" cajas de texto.