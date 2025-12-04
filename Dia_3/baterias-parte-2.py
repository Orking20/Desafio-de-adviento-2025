# A partir de un archivo, que en cada línea contiene una etiqueta
# que representa un banco de batería, hay que encontrar la combinación
# de 12 dígitos que forme el número más grande posible. Ejemplos: 
# 987654321111111 -> 987654321111
# 811111111111119 -> 811111111119
# 234234234234278 -> 434234234278
# 818181911112111 -> 888911112111
# Una vez tengamos todos los números, hay que sumarlos y obtener el resultado final

from manejo_archivos import leer_archivo

# ================ FUNCIONES PRINCIPALES ================
def main() -> None:
    """Función principal del programa."""
    datos = leer_archivo("bancos_baterias.txt")
    #datos = ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]
    resultado = 0

    for linea in datos:
        resultado += num_mas_grande_posible(linea)

    print(resultado)

def num_mas_grande_posible(banco: str, tamano_etiqueta: int = 12) -> int:
    """
    Encuentra el número más grande posible de dos dígitos,
    sin alterar el orden de los números.
    """
    pila = []
    descartes = len(banco) - tamano_etiqueta

    for digito in banco:
        # Mientras pila tenga contenido Y se puedan descartar números Y el último dígito es menor al nuevo
        while pila and descartes > 0 and pila[-1] < digito:
            pila.pop()
            descartes -= 1
        pila.append(digito)

    while descartes > 0:
        pila.pop()
        descartes -= 1

    return conv_int("".join(pila))

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