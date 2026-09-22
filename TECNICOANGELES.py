import os
import sys
import threading
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

def obtener_ruta_abs(ruta_relativa):
    """Obtiene la ruta absoluta para desarrollo y para el ejecutable de PyInstaller."""
    try:
        ruta_base = sys._MEIPASS
    except Exception:
        ruta_base = os.path.abspath(".")
    return os.path.join(ruta_base, ruta_relativa)

def main():
    ruta_base = obtener_ruta_abs(".")
    handler = partial(SimpleHTTPRequestHandler, directory=ruta_base)
    servidor = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    puerto = servidor.server_address[1]
    threading.Thread(target=servidor.serve_forever, daemon=True).start()
    print(f"Aplicación lista en: http://127.0.0.1:{puerto}/index.html")
    servidor.serve_forever()

if __name__ == "__main__":
    main()