# Hay que encontrar la contraseña para abrir una caja fuerte.
# Para descubrir la contraseña contamos con un dial que va del 0 al 99.
# Si la aguja del dial empieza en 0, y la movemos una a la derecha, termina apuntando al 1.
# En cambio, si la movemos 1 a la izquierda, termina apuntando al 99.
# El dial empieza en 50.
# En el archivo 1-dial.txt se encuentra una sucesion de movimientos de la aguja.
# La contraseña es la cantidad de veces que la aguja pasa por cero o termina apuntando al 0.

# ================ FUNCIONES ARCHIVOS ================
def leer_archivo():
    """Lee el archivo con los códigos."""
    with open('dial.txt', 'r') as archivo:
        return archivo.read()

# ================ FUNCIONES PRINCIPALES ================
def main():
    """Función que desenboca todo el programa."""
    estado_inicial = 50 # Estado inicial de la aguja en el dial.
    cont_ceros = 0
    lista_codigos = obtener_codigos()

    for codigo in lista_codigos:
        estado_inicial, contador = mover_aguja(estado_inicial, codigo)
        cont_ceros += contador

    print(f"La contraseña es: {cont_ceros}")

def obtener_codigos():
    """Obtiene los códigos, los guarda en una lista y los devuelve."""
    lista_codigos = []
    aux = ""
    codigos = leer_archivo()

    for codigo in codigos:
        if codigo != "\n":
            aux += codigo
        else:
            lista_codigos.append(aux)
            aux = ""

    return lista_codigos

def mover_aguja(estado_inicial, codigo):
    """Mueve la aguja en la dirección indicada, y una cantidad de veces cómo corresponda.
    Devuelve el número que apunta la aguja al finalizar."""
    try:
        cant_movimientos = int(codigo[1:]) # Selecciono todo el código exceptuando el primer caracter.

        if codigo[0] == 'R': # Derecha
            estado_final, contador = girar_R(estado_inicial, cant_movimientos)
        elif codigo[0] == 'L': # Izquierda
            estado_final, contador = girar_L(estado_inicial, cant_movimientos)

        return estado_final, contador
    except Exception as e:
        print(f"Error: {e}")

def girar_R(estado_inicial, cant_movimientos):
    pos_actual = estado_inicial
    contador = 0

    for i in range(cant_movimientos):
        pos_actual += 1

        if pos_actual == 100:
            pos_actual = 0
            contador += 1

    if pos_actual == 0:
        estado_final = 0
    else:
        estado_final = (estado_inicial + cant_movimientos) % 100
    
    return estado_final, contador

def girar_L(estado_inicial, cant_movimientos):
    pos_actual = estado_inicial
    contador = 0

    for i in range(cant_movimientos):
        pos_actual -= 1

        if pos_actual == 0:
            contador += 1
        if pos_actual == -1:
            pos_actual = 99

    if pos_actual == 0:
        estado_final = 0
    else:
        estado_final = (estado_inicial - cant_movimientos) % 100
    
    return estado_final, contador

if __name__ == "__main__":
    main()