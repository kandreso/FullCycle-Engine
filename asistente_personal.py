import flet as ft
from openai import OpenAI
# ... tus otros imports ...

def main(page: ft.Page):
    page.title = "Secretaria IA"
    # Usamos texto simple para las alineaciones
    page.vertical_alignment = "start" 
    
    chat = ft.ListView(expand=True, spacing=10)

    def procesar_comando(e):
        # ... tu lógica de escucha ...
        
        # AQUÍ ESTÁ EL ARREGLO:
        chat.controls.append(
            ft.Container(
                content=ft.Text("Hola, soy tu secretaria"),
                bgcolor="blue",
                padding=10,
                border_radius=10,
                alignment="center_right" # <--- ESTO NUNCA FALLA
            )
        )
        page.update()

    page.add(ft.Text("Secretaria Lista", size=20), chat)
    # OPCIÓN CORRECTA (Copia y pega esto)
    page.floating_action_button = ft.FloatingActionButton(
    content=ft.Icon(ft.icons.MIC), # Agregamos 'content' explícitamente
    on_click=procesar_comando,
    bgcolor="blue",
    tooltip="Hablar"
)

    page.update()

if __name__ == "__main__":
    ft.app(target=main)
