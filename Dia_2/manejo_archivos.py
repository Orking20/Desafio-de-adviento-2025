from pathlib import Path

# ================ FUNCIONES ARCHIVOS ================
def leer_archivo(ruta: str) -> str:
    """Lee el archivo con los códigos."""
    ruta_dir = Path(__file__).parent
    ruta_archivo = ruta_dir / ruta

    try:
        return ruta_archivo.read_text(encoding='utf-8')
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: el archivo {ruta} no existe.")
    except Exception as e:
        raise Exception(f"Error inesperado al leer el archivo: {e}")