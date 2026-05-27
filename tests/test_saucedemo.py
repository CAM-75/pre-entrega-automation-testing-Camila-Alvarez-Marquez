#Archivo de pruebas en sí.
from utils.helpers import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Primer Punto de la Pre-Entrega, "Automatización de Login".
def test_login(driver):
    #Login automatizado.
    login(driver, "standard_user", "secret_sauce")

    #Validación URL, Products y Swag Labs.
    assert "/inventory.html" in driver.current_url

    title = driver.find_element(By.CLASS_NAME, "title").text
    header = driver.find_element(By.CLASS_NAME, "app_logo").text

    assert title == "Products"
    assert header == "Swag Labs"

#Segundo Punto de la Pre-Entrega, "Navegación y Verificación del Catálogo".
def test_catalogo_productos(driver):
    login(driver, "standard_user", "secret_sauce")

    #Validación de título.
    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products"
    
    #Validación de productos.
    productos = driver.find_elements(By.CSS_SELECTOR, "[data-test='inventory-item']")
    # Nota personal: Es elements porque son varios elementos con la misma nomenclatura, y se buscan por CSS_SELECTOR para que no haya problema si cambia a futuro el nombre de la clase. E inventory-item va en comillas simples, porque las comunes ya las estoy usando para contener las llaves [].

    assert len(productos) > 0

    #Nombre y precio del primer producto.
    nombre_producto = productos[0].find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']").text
    assert nombre_producto == "Sauce Labs Backpack"

    precio_producto = productos[0].find_element(By.CSS_SELECTOR, "[data-test='inventory-item-price']").text
    assert precio_producto == "$29.99"

#Tercer Punto de la Pre-Entrega, "Interacción con Productos".
def test_agregar_carrito(driver):
    login(driver, "standard_user", "secret_sauce")

    wait = WebDriverWait(driver, 10)

    #Agregar al carrito, funcionamiento del botón.
    btn_add = wait.until(
        EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Add to cart')]"))
    )
    btn_add.click()

    #Contador correcto de productos en carrito.
    badge = driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    assert badge.text == "1"
    
    driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-link']").click

    nombre_articulo = driver.find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']").text

    producto_agregado = driver.find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']").text
    assert producto_agregado == nombre_articulo
