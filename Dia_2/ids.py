# Se nos da un archivo con distintos rangos de IDs.
# En estos rangos de IDs pueden haber IDs corruptas.
# Alguien modificó algunas IDs, pero todas las modificadas siguen un patrón de repetición.
# Algunos ejemplos de patrones: 123123, 22222, 121121, 1010, 11, 446446, 38593859
# Hay que encontrar los IDs corruptos y al final sumarlos todos.

from pathlib import Path

# ================ FUNCIONES ARCHIVOS ================
def leer_archivo(ruta: str = 'rangos.txt') -> str:
    """Lee el archivo con los códigos."""
    ruta_dir = Path(__file__).parent
    ruta_archivo = ruta_dir / ruta

    try:
        return ruta_archivo.read_text(encoding='utf-8')
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: el archivo {ruta} no existe.")
    except Exception as e:
        raise Exception(f"Error inesperado al leer el archivo: {e}")

# ================ FUNCIONES PRINCIPALES ================
def main() -> None:
    """Función principal del programa."""
    rangos = leer_archivo().split(',')
    #rangos = ['11-22', '95-115', '998-1012', '1188511880-1188511890', '222220-222224', '1698522-1698528', '446443-446449', '38593856-38593862', '565653-565659', '824824821-824824827', '2121212118-2121212124']
    #rangos = ['3-17']
    ids_corruptos = []
    resultado = 0
    procesar_ids(rangos, ids_corruptos)

    for num in ids_corruptos:
        resultado += int(num)

    print(resultado)

def procesar_ids(rangos: list[str], ids_corruptos: list[str]) -> list[str]:
    for rango in rangos:
        rango = rango.split('-')
        inicio = int(rango[0])
        fin = int(rango[1])

        for num in range(inicio, fin + 1):
            if todos_iguales(str(num)) and len(str(num)) > 1:
                ids_corruptos.append(str(num))
            else:
                id_invalida = buscar_patron(str(num))
                if id_invalida != None:
                    ids_corruptos.append(id_invalida)

    return ids_corruptos

def todos_iguales(numero: str | list[str]) -> bool:
    """Devuelve True si el string tiene todos los caracteres iguales."""
    return len(set(numero)) == 1

def buscar_patron(numero: str) -> str:
    """Separa el número en bloques para encontrar un patrón de repetición.
    Devuelve el número de id inválido si encuentra un patrón, y None si no lo encuentra."""
    bloques = []
    inicio = 0
    tamano_bloque = 2

    #if len(numero) // 2 <= tamano_bloque:
    for _ in range(len(numero) // 2):
        while inicio < len(numero): # Lógica para separar en bloques
            bloque = numero[inicio:inicio + tamano_bloque]
            bloques.append(bloque)
            inicio += tamano_bloque
        if len(bloques) > 1 and todos_iguales(bloques):
            return numero
        else:
            bloques = []
            inicio = 0
            tamano_bloque += 1

if __name__ == '__main__':
    main()