import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    grid = input_data[2:2+n]
    
    h_row, h_col = -1, -1
    quesos_totales = 0
    
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 'H':
                h_row, h_col = r, c
            elif grid[r][c] == 'Q':
                quesos_totales += 1
                
    if quesos_totales == 0:
        print(-1)
        return

    # 1. Verificar si ya hay algún queso inalcanzable (respuesta 0)
    visited = [[False]*m for _ in range(n)]
    queue = deque([(h_row, h_col)])
    visited[h_row][h_col] = True
    alcanzados = 0
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                if grid[nr][nc] == 'Q':
                    visited[nr][nc] = True
                    alcanzados += 1
                    queue.append((nr, nc))
                    
    if alcanzados < quesos_totales:
        print(0)
        return

    # Si todos los quesos son alcanzables de base, el costo mínimo para aislar uno
    # estará acotado por la cantidad de vecinos del Hongo o los vecinos de un queso individual (máximo 4).
    # Hacemos una búsqueda exhaustiva BFS de corte mínimo (Min-Cut con capacidad en nodos).
    # Dado que la respuesta máxima es pequeña (<= 4), podemos evaluar removiendo combinaciones
    # de vecinos directos del Hongo o usando un algoritmo simplificado de flujo.
    
    # Obtenemos los vecinos directos del hongo que contienen Queso
    vecinos_hongo = []
    for i in range(4):
        nr, nc = h_row + dr[i], h_col + dc[i]
        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 'Q':
            vecinos_hongo.append((nr, nc))
            
    # Si quitamos todos los vecinos del hongo, ningún queso será alcanzable.
    # Por ende, la respuesta máxima posible es la cantidad de vecinos funcionales del Hongo.
    ans = len(vecinos_hongo)
    if ans == 0:
        print(-1)
        return

    # Evaluamos si removiendo solo 1 queso o menos es posible desconectar la grilla
    # (Buscamos si hay un punto de articulación estratégico)
    def test_desconexion(removidos):
        v = [[False]*m for _ in range(n)]
        for rr, cc in removidos:
            v[rr][cc] = True
        q = deque([(h_row, h_col)])
        v[h_row][h_col] = True
        alc = 0
        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < n and 0 <= nc < m and not v[nr][nc]:
                    if grid[nr][nc] == 'Q':
                        v[nr][nc] = True
                        alc += 1
                        q.append((nr, nc))
        # Si la cantidad de alcanzados más los removidos es menor que el total, logramos aislar algo
        return alc + len(removidos) < quesos_totales

    # Probamos si removiendo 1 vecino se puede lograr
    if ans > 1:
        for cand in vecinos_hongo:
            if test_desconexion([cand]):
                ans = 1
                break
                
    # Probamos si removiendo 2 vecinos se puede lograr (en caso de que ans siga siendo mayor)
    if ans > 2:
        from itertools import combinations
        for cand1, cand2 in combinations(vecinos_hongo, 2):
            if test_desconexion([cand1, cand2]):
                ans = 2
                break

    print(ans)

if __name__ == '__main__':
    solve()