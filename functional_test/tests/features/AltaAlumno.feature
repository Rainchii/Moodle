Feature: Como usuario requiro darme de alta en el sistema
	para hacer modificaciones a la cuenta el sistema.

Scenario: Verificar que la inscripcion del usario se complete exitosamante.
	Given Ingresar en el navegador la url "http://192.168.0.23:8000/alumnos/nuevoA/" en la barra de direcciones
	When Introduzca el texto "user" en el campo Username, el texto "password" en el campo contraseña, el texto "nombre" en el campo Nombre, el texto "apellido" en el campo Apellidos, el texto "mail@hotmail.com" en el campo E-mail y oprimo la tecla Enter
	Then Puedo ver en el titulo del navegador la palabra "Login Moodle".

Scenario: Verificar que la inscripcion del usario se complete exitosamante.
	Given Ingresar en el navegador la url "http://192.168.0.23:8000/alumnos/nuevoA/" en la barra de direcciones
	When Introduzca el texto "Car" en el campo Username, el texto "contra" en el campo contraseña, el texto "Carlos" en el campo Nombre, el texto "Perez" en el campo Apellidos, el texto "perez@hotmail.com" en el campo E-mail y oprimo la tecla Enter
	Then Puedo ver en el titulo del navegador la palabra "Login Moodle".

Scenario: Verificar que la inscripcion del usario se complete exitosamante.
	Given Ingresar en el navegador la url "http://192.168.0.23:8000/alumnos/nuevoA/" en la barra de direcciones
	When Introduzca el texto "LuS" en el campo Username, el texto "psw" en el campo contraseña, el texto "Luis" en el campo Nombre, el texto "Valle" en el campo Apellidos, el texto "valle@hotmail.com" en el campo E-mail y oprimo la tecla Enter
	Then Puedo ver en el titulo del navegador la palabra "Login Moodle".
