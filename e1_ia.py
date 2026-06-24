import sys

def solucion_a():
    # Leer la palabra de la entrada estándar y quitarle saltos de línea molestos
    nombre = sys.stdin.read().strip()
    # Imprimir el mensaje en el formato exacto requerido
    print(f"Hello {nombre}!")

if __name__ == '__main__':
    solucion_a()
