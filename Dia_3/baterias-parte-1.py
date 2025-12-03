# A partir de un archivo, que en cada línea contiene una etiqueta
# que representa un banco de batería, hay que encontrar la combinación
# de 2 dígitos que forme el número más grande posible. Ejemplos: 
# 987654321111111 -> 98
# 811111111111119 -> 89
# 234234234234278 -> 78
# 818181911112111 -> 92
# Una vez tengamos todos los números, hay que sumarlos y obtener el resultado final

from pathlib import Path

# ================ FUNCIONES ARCHIVOS ================
def leer_archivo(ruta: str = 'bancos_baterias.txt') -> str:
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
    #datos = ["81119"]
    resultado = 0

    for linea in datos:
        resultado += num_mas_grande_posible(linea)

    print(resultado)

def num_mas_grande_posible(banco: str) -> int:
    """
    Encuentra el número más grande posible de dos dígitos,
    sin alterar el orden de los números.
    """
    numero_final = None

    num_1 = max(banco)
    pos_1 = banco.index(num_1)
    banco_aux: str = banco.replace(num_1, "", 1)

    if num_1 in banco_aux:
        num_2 = max(banco_aux)
        numero_final = num_1 + num_2
    else:
        num_2 = sorted(set(banco), reverse=True)[1] # Encuentra el segundo número más alto
        pos_2 = banco.index(num_2)

        if pos_1 < pos_2 or num_1 == num_2:
            numero_final = num_1 + num_2
        else:
            if pos_1 + 1 == len(banco): # Si el número más grande está en la última posición
                numero_final = num_2 + num_1
            else:
                banco_aux = banco[pos_1 + 1:]
                num_2 = max(banco_aux)
                numero_final = num_1 + num_2

    return conv_int(numero_final)

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