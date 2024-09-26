from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#C:\Users\<user>\.wdm\drivers\chromedriver\<version>
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def automate_task(url, element_id):
    # Configuración de las opciones de Chrome
    chrome_options = Options()
    #chrome_options.add_argument("--disable-usb")

    #chrome_options.add_argument("--headless")  # Opcional: Ejecutar en modo headless (sin interfaz gráfica)

    # Inicializa el navegador Chrome con webdriver-manager, sin necesidad de especificar la ruta del driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Navegar a la URL
    driver.get(url)

    # Esperar a que la página cargue completamente
    time.sleep(5)

    try:
        # Localizar el elemento por su ID
        element = driver.find_element("id", element_id)
        
        # Desplazar el elemento al centro de la pantalla
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

        # Espera un segundo para asegurarse de que el scroll ha terminado
        time.sleep(1)

        # Capturar el elemento como imagen
        element.screenshot(f'{element_id}_screenshot.png')
        print(f'Captura guardada como {element_id}_screenshot.png')

    except Exception as e:
        print(f"Error al capturar el elemento: {e}")

    # Cerrar el navegador
    driver.quit()

# Ejemplo de uso
automate_task("https://www.copaair.com/es-pa/todos-los-temas/", "__next")
