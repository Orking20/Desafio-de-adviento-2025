# Se nos da un archivo con una grilla con muchos rollos de papel.
# Debemos seleccionar los rollos de papel que sean adyacentes a
# menos de otros cuatro rollos de papel, en todas las direcciones (N, S, E, O, NE, NO, SE, SO)
# Finalmente, mostrar la cantidad de rollos de papel seleccionados.

from pathlib import Path

# ================ FUNCIONES ARCHIVOS ================
def leer_archivo(ruta: str = 'rollos_papel.txt') -> str:
    """Lee el archivo con los códigos."""
    ruta_dir = Path(__file__).parent
    ruta_archivo = ruta_dir / ruta

    try:
        return ruta_archivo.read_text(encoding='utf-8').splitlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: el archivo {ruta} no existe.")
    except Exception as e:
        raise Exception(f"Error inesperado al leer el archivo: {e}")

# ================ FUNCIONES PRINCIPALES ================
def main() -> None:
    """Función principal del programa."""
    datos = leer_archivo()
    print(contar_rollos_accesibles(datos))

def contar_rollos_accesibles(lineas: list[str]):
    filas = len(lineas)
    columnas = len(lineas[0])

    # Se convierte cada línea en una lista de caracteres quitando el salto de línea
    grilla = []
    for linea in lineas:
        linea_sin_salto = linea.rstrip()
        caracteres = list(linea_sin_salto)
        grilla.append(caracteres)

    # Movimientos relativos para las 8 posiciones vecinas
    vecinos_offset = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]

    rollos_accesibles = 0

    for fila in range(filas):
        for col in range(columnas):
            # Si no hay un rollo, continuamos
            if grilla[fila][col] != '@':
                continue

            cantidad_vecinos = 0

            for mov_fil, mov_col in vecinos_offset:
                fila_vecina = fila + mov_fil
                col_vecina = col + mov_col

                # Verificar que la posición vecina esté dentro de la grilla
                if fila_vecina >= 0 and fila_vecina < filas and col_vecina >= 0 and col_vecina < columnas:
                    if grilla[fila_vecina][col_vecina] == '@':
                        cantidad_vecinos += 1

            if cantidad_vecinos < 4:
                rollos_accesibles += 1

    return rollos_accesibles

if __name__ == '__main__':
    main()