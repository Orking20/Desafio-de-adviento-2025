# Se nos da un archivo con una grilla con muchos rollos de papel.
# Debemos seleccionar y eliminar los rollos de papel que sean adyacentes a
# menos de otros cuatro rollos de papel, en todas las direcciones (N, S, E, O, NE, NO, SE, SO)
# Finalmente, mostrar la cantidad de rollos de papel eliminados.

from manejo_archivos import leer_archivo

# ================ VARIABLES GLOBALES ================
grilla = []
rollos_seleccionados = []
cont_rollos_accesibles = 0
seguir = True # Indica si una vez eliminados todos los rollos hay que seguir revisando si quedan más por eliminar

# ================ FUNCIONES PRINCIPALES ================
def main() -> None:
    """Función principal del programa."""
    datos = leer_archivo("rollos_papel.txt")
    lineas = armar_grilla(datos)

    while seguir:
        (cont_rollos_accesibles, rollos_seleccionados) = encontrar_rollos_accesibles(lineas)
        eliminar_rollos_accesibles(rollos_seleccionados)

    print(cont_rollos_accesibles)

def armar_grilla(lineas: list[str]) -> list[str]:
    """Se convierte cada línea en una lista de caracteres quitando el salto de línea"""
    for linea in lineas:
        linea_sin_salto = linea.rstrip()
        caracteres = list(linea_sin_salto)
        grilla.append(caracteres)
    return lineas

def encontrar_rollos_accesibles(lineas: list[str]) -> tuple[int, list[tuple[int, int]]]:
    """Encuentra los rollos accesibles"""
    global cont_rollos_accesibles
    global seguir
    filas = len(lineas)
    columnas = len(lineas[0])
    seguir = False

    # Movimientos relativos para las 8 posiciones vecinas
    vecinos_offset = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]

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
                cont_rollos_accesibles += 1
                rollos_seleccionados.append((fila, col))
                seguir = True

    return (cont_rollos_accesibles, rollos_seleccionados)

def eliminar_rollos_accesibles(rollos_seleccionados: list[tuple[int, int]]):
    """Elimina los rollos seleccionados de la grilla."""
    # Rollo tendría una lista parecida a [(0,0), (0,1), (2,5)] con coordenadas a eliminar
    for rollo in rollos_seleccionados:
        fila = rollo[0]
        col = rollo[1]
        grilla[fila][col] = '.'

if __name__ == '__main__':
    main()