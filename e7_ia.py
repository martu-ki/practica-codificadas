import sys

def es_posible(d, n, k, personas, bodegas, capacidades):
    # Intentamos emparejar de forma Greedy (Ávida) de izquierda a derecha
    p_idx = 0
    for i in range(k):
        cap_restante = capacidades[i]
        b_pos = bodegas[i]
        # Atendemos a todas las personas posibles que estén dentro del rango [b_pos - d, b_pos + d]
        while p_idx < n and abs(personas[p_idx] - b_pos) <= d and cap_restante > 0:
            p_idx += 1
            cap_restante -= 1
    return p_idx == n

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    
    personas = sorted([int(x) for x in input_data[2:2+n]])
    bodegas_raw = [int(x) for x in input_data[2+n:2+n+k]]
    capacidades_raw = [int(x) for x in input_data[2+n+k:2+n+2*k]]
    
    # Ordenamos conjuntamente las bodegas y sus capacidades según su posición en el eje X
    bodegas_zip = sorted(zip(bodegas_raw, capacidades_raw))
    bodegas = [b for b, c in bodegas_zip]
    capacidades = [c for b, c in bodegas_zip]
    
    # Búsqueda binaria en el rango de distancias válidas [0, 10^9]
    low = 0
    high = 10**9
    ans = high
    
    while low <= high:
        mid = (low + high) // 2
        if es_posible(mid, n, k, personas, bodegas, capacidades):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    print(ans)

if __name__ == '__main__':
    solve()