"""
Pre Entrega de Automatización QA - Talento Tech

Ejercicios de automatización en la página "Saucedemo" (https://www.saucedemo.com/):
* Comprobar ciertas funcionalidades básicas de la página, mediante pruebas unitarias automatizadas.

Documentos trabajados:

* Carpeta Pre Entrega:
        ** conftest.py
        ** README.md
        ** reporte.html
        ** requirements.txt
    * Carpeta tests:
        ** test_saucedemo.py
    * Carpeta utils:
        ** helpers.py

Alumna: Álvarez Márquez, Camila

Autoridades: Arribillaga, Amancay  y Farfán, Brayann

Fecha: 1° Cuatrimestre, 2026

* Tests:
    ** Login exitoso
        *** Validación URL, header y título de la página.

    ** Navegación y verificación del catálogo
	    *** Validación de productos.
	    *** Comprobación del nombre y precio del primer producto de la lista de artículos.

    ** Comportamiento del carrito (Agregar artículo)
	    *** Funcionamiento del botón de "Add to cart".
	    *** Comprobación del contador de productos en el carrito (1).
	    *** Igualdad entre los nombres del producto agregado al carrito y del artículo en la lista de artículos de la página.

* Para llevar a cabo la Pre Entrega se utilizó VSC, Python, Pytest, Pytest- HTML, Selenium, WebDriver, Chrome (para realizar los tests) y HTML (reporte).

"""