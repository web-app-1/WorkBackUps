import tkinter as tk
from tkinter import messagebox
import ctypes  # Para ajustar el DPI en pantallas con alta resolución
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Ajuste del DPI para mejorar la nitidez en Windows
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception as e:
    print(f"Error al ajustar DPI: {e}")

def run_selenium_script():
    # Obtiene la URL y los valores ingresados por el usuario
    url = url_entry.get()
    search_type = search_type_var.get()
    search_value = search_value_entry.get()

    # Validar que los campos no estén vacíos
    if not url or not search_value:
        messagebox.showwarning("Check", "Please enter a valid URL and HTML element (ID or Class).")
        return

    # Configuración de las opciones de Chrome
    chrome_options = Options()
    #chrome_options.add_argument("--headless")  # Ejecutar en modo headless (sin interfaz gráfica)

    # Inicializa el navegador Chrome con webdriver-manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Navegar a la URL
        driver.get(url)
        time.sleep(3)  # Espera a que la página cargue completamente

        # Buscar elemento por ID o Clase
        if search_type == "ID":
            element = driver.find_element(By.ID, search_value)
        elif search_type == "Class":
            element = driver.find_element(By.CLASS_NAME, search_value)

        # Desplazar el elemento al centro de la pantalla
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

        # Capturar el elemento como imagen
        element.screenshot(f'{search_value}_screenshot.png')
        messagebox.showinfo("Process Completed", f'Capture saved as {search_value}_screenshot.png')

    except Exception as e:
        messagebox.showerror("Error", f"Element not found: {e}")
    
    # Cierra el navegador
    driver.quit()

# Crear la ventana principal
window = tk.Tk()
window.title("Image Scraping PROTO")
window.geometry("700x350")
window.configure(bg="#f0f0f0")

# Fuente personalizada
title_font = ("Helvetica", 12, "bold")
label_font = ("Helvetica", 12)

# Título
title_label = tk.Label(window, text="HTML Elements Capture", font=title_font, bg="#f0f0f0", fg="#333")
title_label.pack(pady=10)

# Frame para la entrada de la URL
url_frame = tk.Frame(window, bg="#f0f0f0")
url_frame.pack(pady=10)

url_label = tk.Label(url_frame, text="URL:", font=label_font, bg="#f0f0f0", fg="#333")
url_label.grid(row=0, column=0, padx=10, pady=5)

url_entry = tk.Entry(url_frame, width=35)
url_entry.grid(row=0, column=1, padx=10, pady=5)

# Frame para seleccionar entre ID o Clase
search_type_var = tk.StringVar(value="ID")

search_type_frame = tk.Frame(window, bg="#f0f0f0")
search_type_frame.pack(pady=10)

search_type_label = tk.Label(search_type_frame, text="Search By:", font=label_font, bg="#f0f0f0", fg="#333")
search_type_label.grid(row=0, column=0, padx=10)

radio_id = tk.Radiobutton(search_type_frame, text="ID", variable=search_type_var, value="ID", bg="#f0f0f0", font=label_font)
radio_id.grid(row=0, column=1, padx=10)

radio_class = tk.Radiobutton(search_type_frame, text="Class", variable=search_type_var, value="Class", bg="#f0f0f0", font=label_font)
radio_class.grid(row=0, column=2, padx=10)

# Frame para la entrada del ID o Clase
search_value_frame = tk.Frame(window, bg="#f0f0f0")
search_value_frame.pack(pady=10)

search_value_label = tk.Label(search_value_frame, text="ID or Class:", font=label_font, bg="#f0f0f0", fg="#333")
search_value_label.grid(row=0, column=0, padx=10, pady=5)

search_value_entry = tk.Entry(search_value_frame, width=35)
search_value_entry.grid(row=0, column=1, padx=10, pady=5)

# Botón para ejecutar la automatización
run_button = tk.Button(window, text="Run", command=run_selenium_script, bg="#4CAF50", fg="white", font=label_font)
run_button.pack(pady=20)

# Ejecutar la ventana principal
window.mainloop()
