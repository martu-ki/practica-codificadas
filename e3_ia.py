import sys

def solucion_c():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    idx = 1
    
    palabras_por_persona = []
    frecuencia_global = {}
    
    for _ in range(n):
        p = int(input_data[idx])
        idx += 1
        palabras_actuales = set()
        for _ in range(p):
            palabra = input_data[idx]
            idx += 1
            palabras_actuales.add(palabra)
            # Acumular la frecuencia total
            frecuencia_global[palabra] = frecuencia_global.get(palabra, 0) + 1
        palabras_por_persona.append(palabras_actuales)
        
    if not palabras_por_persona:
        return
        
    # Encontrar la intersección de palabras usadas por todos
    comunes = palabras_por_persona[0]
    for s in palabras_por_persona[1:]:
        comunes = comunes.intersection(s)
        
    # Filtrar frecuencias de las palabras comunes
    resultado = [(palabra, frecuencia_global[palabra]) for palabra in comunes]
    
    # Criterio de ordenación:
    # 1. Mayor frecuencia primero (-frecuencia)
    # 2. Orden lexicográfico descendente (la palabra misma al revés no sirve de forma directa en strings, 
    #    pero en Python podemos usar una tupla de ordenación personalizada o usar la palabra en sí con reverso)
    # Para ordenar strings al revés de manera descendente de forma secundaria con un valor numérico primario,
    # ordenamos convencionalmente aplicando llaves de ordenación:
    resultado.sort(key=lambda x: (-x[1], x[0]), reverse=False)
    
    # Nota analítica sobre el orden secundario: El problema pide que si hay empate en frecuencia,
    # la palabra lexicográficamente mayor aparezca antes (ej. "zorro" antes que "abeja").
    # Al ordenar por (-frecuencia, x[0]), las frecuencias menores (que son en realidad más grandes por el signo menos)
    # se posicionan primero de forma ascendente. Como queremos el string de manera descendente (mayor a menor),
    # podemos usar una ordenación por etapas o usar una función que invierta los caracteres para simular un valor negativo.
    # Una forma directa en Python aprovechando que el alfabeto es pequeño:
    
    def criterio(item):
        palabra, frec = item
        # Frecuencia descendente (-frec)
        # Palabra descendente (podemos convertir cada carácter a su valor negativo de ord)
        return (-frec, [-ord(c) for c in palabra])
        
    resultado.sort(key=criterio)
    
    for palabra, _ in resultado:
        print(palabra)

if __name__ == '__main__':
    solucion_c()