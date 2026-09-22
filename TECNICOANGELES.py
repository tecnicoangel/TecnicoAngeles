import os
import sys
import webview

def obtener_ruta_abs(ruta_relativa):
    """Obtiene la ruta absoluta para desarrollo y para el ejecutable de PyInstaller."""
    try:
        ruta_base = sys._MEIPASS
    except Exception:
        ruta_base = os.path.abspath(".")
    return os.path.join(ruta_base, ruta_relativa)

def main():
    # Obtener la ruta del archivo HTML principal
    html_path = obtener_ruta_abs("index.html")
    
    # Crear la ventana con soporte para cargar archivos locales y estilos
    window = webview.create_window(
        title="TecnicoAngel - Sistema de Gestión", 
        url=f"file://{html_path}",
        width=1280,
        height=800,
        resizable=True
    )
    
    # Activar opciones para la carga correcta de activos locales
    webview.start(gui='qt' if sys.platform == 'win32' else None)

if __name__ == "__main__":
    main()