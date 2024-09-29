
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from services import service_logic
from datetime import datetime
import flet as ft
import threading
import time


# Función para actualizar la hora en tiempo real
def update_time(label):
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        label.value = f"Hora en tiempo real: {current_time}"
        label.update()
        time.sleep(1)

def main(page: ft.Page):
    page.title = "Generador de archivos"
    page.window_width = 600
    page.window_height = 200
    page.window.center = True  # Ventana centrada en la pantalla

    # Configuración del contenedor principal
    contenedor = ft.Column(
        [
            ft.Row(
                controls=[
                    ft.ElevatedButton("Extraer datos desde Excel", on_click=service_logic.instancia_automática),
                    ft.ElevatedButton("Ingreso manual", on_click=lambda e: print("Ingreso manual...")),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=50
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,  # Centrado vertical
    )
    
    # Espacio para la hora en tiempo real
    hora_label = ft.Text("Hora: ")
    time_container = ft.Container(
        content=hora_label,
        alignment=ft.alignment.bottom_left,
        padding=ft.padding.all(10)
    )
    
    # Espacio para el logo en la esquina inferior derecha
    logo_container = ft.Container(
        content=ft.Text(""),
        alignment=ft.alignment.bottom_right,
        padding=ft.padding.all(10)
    )

    # Agregar los controles a la página
    page.add(contenedor)
    page.add(ft.Row([time_container, logo_container], alignment=ft.MainAxisAlignment.SPACE_BETWEEN))

    # Hilo para actualizar la hora
    threading.Thread(target=update_time, args=(hora_label,), daemon=True).start()

# Ejecutar la aplicación Flet
ft.app(target=main)
