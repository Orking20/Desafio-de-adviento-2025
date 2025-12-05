# Tenemos un archivo de entrada que está dividido en tres partes:
# La primera parte son rangos de ID de ingredientes en estado fresco.
# La segunda parte es una línea en blanco separadora.
# La tercera parte son los ID de los ingredientes.
# Hay que descubrir el total de ingredientes frescos,
# ignorando la segunda y tercera parte del archivo.

from manejo_archivos import leer_archivo

# ================ FUNCIONES PRINCIPALES ================
def main() -> None:
    """Función principal del programa."""
    datos = leer_archivo("id_ingredientes.txt")

    rangos = separar_datos(datos)
    resultado = contar_ing_frescos(rangos)

    print(resultado)

def separar_datos(datos: list[str]) -> set[str]:
    """A partir de los datos indicados, se separan y devuelven los rangos."""
    rangos = []

    # Recuperamos solo los rangos de IDs
    for linea in datos:
        if linea == "":
            break
        rangos.append(linea)

    return set(rangos) # Se eliminan los duplicados

def contar_ing_frescos(rangos: set[str]) -> int:
    """A partir de los rangos de ID se cuentan el total de ingredientes frescos."""
    intervalos = []

    # Parseamos a intervalos numéricos
    for rango in rangos:
        (inicio, fin) = separar_rangos(rango)
        intervalos.append((inicio, fin))

    intervalos.sort() # Ordenamos por inicio

    # Merge de intervalos
    fucionado = []
    (ini_actual, fin_actual) = intervalos[0]
    # ["3-5", "10-14", "12-18", "16-20"]
    # ["3-5", "10-14", "10-20"]
    for inicio, fin in intervalos[1:]:
        if inicio <= fin_actual + 1:
            # Se solapan -> extendemos el intervalo actual
            fin_actual = max(fin_actual, fin)
        else:
            # No se solapan -> guardamos intervalo y empezamos otro
            fucionado.append((ini_actual, fin_actual))
            ini_actual = inicio
            fin_actual = fin

    # Agregamos el último
    fucionado.append((ini_actual, fin_actual))

    # Sumamos longitudes
    total = 0
    for intervalo in fucionado:
        inicio = intervalo[0]
        fin = intervalo[1]
        total += (fin - inicio + 1)

    return total

def separar_rangos(rango: str) -> tuple[int, int]:
    """Separa el ID inicial del final de un rango."""
    # Separamos los ID de los rangos quedando: ['120', '146']
    rango_seleccionado: list[str] = rango.split('-')

    # Convertimos los rangos de ID a enteros para poder recorrerlos
    for i in range(len(rango_seleccionado)):
        if i == 0:
            inicio = conv_int(rango_seleccionado[i])
        if i == 1:
            fin = conv_int(rango_seleccionado[i])

    return (inicio, fin)

def conv_int(string: str) -> int:
    """Convierte un string a entero."""
    try:
        return int(string)
    except ValueError:
        raise ValueError(f"El string '{string}' no se puede converitr a número entero.")
    except Exception as e:
        raise Exception(f"Error inesperado: {e}")

if __name__ == '__main__':
    main()