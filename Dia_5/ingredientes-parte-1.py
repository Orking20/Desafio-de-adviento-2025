# Tenemos un archivo de entrada que está dividido en tres partes:
# La primera parte son rangos de ID de ingredientes en estado fresco.
# La segunda parte es una línea en blanco separadora.
# La tercera parte son los ID de los ingredientes que hay que
# comprobar en que estado se encuentran.
# Los ID fuera de los rangos están vencidos o en mal estado.
# Hay que descubrir cuántos de estos ingredientes están frescos.

from manejo_archivos import leer_archivo

# ================ FUNCIONES PRINCIPALES ================
def main() -> None:
    """Función principal del programa."""
    datos = leer_archivo("id_ingredientes.txt")
    (rangos, ingredientes) = separar_datos(datos)
    ingredientes = conv_ingredientes(ingredientes)
    resultado = contar_ing_frescos(rangos, ingredientes)

    print(resultado)

def separar_datos(datos: list[str]) -> tuple[list[str], list[str]]:
    """
    A partir de los datos indicados, separa los rangos
    de ID de los ID de ingredientes.
    """
    rangos = []
    ingredientes = []
    corte = False

    for linea in datos:
        if linea == "":
            corte = True
            continue

        # Después del corte, pasan a agregarse a los ingredientes
        if not corte and linea != "\n":
            rangos.append(linea)
        else:
            ingredientes.append(linea)

    # Se eliminan los duplicados
    rangos = set(rangos)
    ingredientes = set(ingredientes)

    return (rangos, ingredientes)

def conv_ingredientes(ingredientes: list[str]) -> list[int]:
    """Convierte la lista de ingredientes a una lista de números enteros."""
    ing_int = []

    for ingrediente in ingredientes:
        ing_int.append(conv_int(ingrediente))

    return ing_int

def contar_ing_frescos(rangos: list[str], ingredientes: list[int]) -> int:
    """
    A partir de los rangos de ID y de los ingredientes,
    cuenta cuántos ingredientes frescos hay.
    """
    cont_frescos = 0

    # Recorremos los ingredientes y contamos si los que están frescos
    for ingrediente in ingredientes:
        for rango in rangos:
            # Separamos los ID de los rangos quedando: ['120', '146']
            rango_seleccionado: list[str] = rango.split('-')

            # Convertimos los rangos de ID a enteros para poder recorrerlos
            for i in range(len(rango_seleccionado)):
                if i == 0:
                    inicio = conv_int(rango_seleccionado[i])
                if i == 1:
                    fin = conv_int(rango_seleccionado[i])

            if ingrediente in range(inicio, fin + 1):
                cont_frescos += 1
                break

    return cont_frescos

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