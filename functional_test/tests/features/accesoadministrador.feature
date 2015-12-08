Feature: Como programador del proyecto
		quiero acceder a la pagina de administrador de Django
		para poder saber si se creo el super usuario (Docente)

Scenario: Verificar la creacion del super usuario
	Given Ingresar en el navegador la url "http://10.1.39.176:8000/admin/login/?next=/admin/" en la barra de direcciones
	When Introduzco el texto "moodle" en el campo Username, el texto "moodle" en el campo Password y oprimo la tecla Enter
	Then Puedo ver en el titulo del navegador la palabra "Administración del sitio | Sitio de administración de Django".

Scenario: Verificar la creacion del super usuario
	Given Ingresar en el navegador la url "http://10.1.39.176:8000/admin/login/?next=/admin/" en la barra de direcciones
	When Introduzco el texto "moodle1" en el campo Username, el texto "moodle1" en el campo Password y oprimo la tecla Enter
	Then Puedo ver en el titulo del navegador la palabra "Administración del sitio | Sitio de administración de Django".

Scenario: Verificar la creacion del super usuario
	Given Ingresar en el navegador la url "http://10.1.39.176:8000/admin/login/?next=/admin/" en la barra de direcciones
	When Introduzco el texto "moodle2" en el campo Username, el texto "moodle2" en el campo Password y oprimo la tecla Enter
	Then Puedo ver en el titulo del navegador la palabra "Administración del sitio | Sitio de administración de Django".