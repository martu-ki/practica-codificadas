import sys

def resolver():
    lineas_entrada = sys.stdin.read().splitlines()
    if not lineas_entrada:
        return
    
    filas, columnas = map(int, lineas_entrada[0].split())
    grilla = lineas_entrada[1:filas+1]
    
    # Buscamos los límites (bounding box) geométricos de la flor
    min_fila, max_fila = filas, -1
    min_col, max_col = columnas, -1
    
    for f in range(filas):
        for c in range(columnas):
            if grilla[f][c] == '*':
                if f < min_fila: min_fila = f
                if f > max_fila: max_fila = f
                if c < min_col: min_col = c
                if c > max_col: max_col = c
                
    # Evaluamos el comportamiento de la mitad inferior de la estructura
    fila_media = (min_fila + max_fila) // 2
    
    # En la forma de 2 (Double Petal), existe un tramo vertical al extremo izquierdo inferior.
    # En la forma de 3 (Triple Corolla), el extremo izquierdo inferior está vacío.
    es_doble_petalo = False
    for f in range(fila_media + 1, max_fila):
        if grilla[f][min_col] == '*':
            es_doble_petalo = True
            break
            
    if es_doble_petalo:
        print("Double Petal Flower")
    else:
        print("Triple Corolla Flower")

if __name__ == '__main__':
    resolver()