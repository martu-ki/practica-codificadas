import sys

def solucion_b():
    # Leer el texto completo
    texto = sys.stdin.read().strip()
    
    # Contar la ocurrencia de cada letra
    cant_t = texto.count('T')
    cant_c = texto.count('C')
    cant_s = texto.count('S')
    
    # Comprobar si las tres cantidades son iguales
    if cant_t == cant_c == cant_s:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solucion_b()