# Hay que encontrar la contraseña para abrir una caja fuerte.
# Para descubrir la contraseña contamos con un dial que va del 0 al 99.
# Si la aguja del dial empieza en 0, y la movemos una a la derecha, termina apuntando al 1.
# En cambio, si la movemos 1 a la izquierda, termina apuntando al 99.
# El dial empieza en 50.
# En el archivo 1-dial.txt se encuentra una sucesion de movimientos de la aguja.
# La contraseña es la cantidad de veces que la aguja pasa por cero o termina apuntando al 0.

from manejo_archivos import leer_archivo

# ================ FUNCIONES PRINCIPALES ================
def main() -> None:
    """Función principal del programa."""
    pos_actual = 50 # Estado inicial de la aguja en el dial.
    cont_ceros = 0
    codigos: list[str] = leer_archivo("dial.txt")

    for codigo in codigos:
        pos_actual, contador = mover_aguja(pos_actual, codigo)
        cont_ceros += contador

    print(f"La contraseña es: {cont_ceros}")

def mover_aguja(pos_actual: int, codigo: str) -> tuple[int, int]:
    """Mueve la aguja en la dirección indicada, y una cantidad de veces cómo corresponda.
    Devuelve el número que apunta la aguja al finalizar."""
    try:
        cant_movimientos = int(codigo[1:]) # Selecciono todo el código exceptuando el primer caracter.

        if codigo[0] == 'R': # Derecha
            estado_final, contador = girar_R(pos_actual, cant_movimientos)
        elif codigo[0] == 'L': # Izquierda
            estado_final, contador = girar_L(pos_actual, cant_movimientos)
        else:
            print(f"Error de dirección en código '{codigo}'")

        return estado_final, contador
    except ValueError:
        raise ValueError(f"El código {codigo[1:]} no se puede converitr a entero.")
    except Exception as e:
        raise Exception(f"Error inesperado: {e}")

def girar_R(pos_actual: int, cant_movimientos: int) -> tuple[int, int]:
    """Cuenta todas las veces que la aguja pasa por el cero, girando el dial a la derecha."""
    contador = 0

    for _ in range(cant_movimientos):
        pos_actual += 1

        if pos_actual == 100:
            pos_actual = 0
            contador += 1

    return pos_actual, contador

def girar_L(pos_actual: int, cant_movimientos: int) -> tuple[int, int]:
    """Cuenta todas las veces que la aguja pasa por el cero, girando el dial a la izquierda."""
    contador = 0

    for _ in range(cant_movimientos):
        pos_actual -= 1

        if pos_actual == 0:
            contador += 1
        if pos_actual == -1:
            pos_actual = 99

    return pos_actual, contador

if __name__ == "__main__":
    main()