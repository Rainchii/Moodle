function eliminarCiudad(ciudad,url) {
	if (confirm("Deseas eliminar la ciudad: "+ciudad)) {
		window.location=url;
	}
}