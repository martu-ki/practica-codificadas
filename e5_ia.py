import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    points = []
    idx = 1
    for _ in range(n):
        x = int(input_data[idx])
        y = int(input_data[idx+1])
        points.append((x, y))
        idx += 2
        
    vistos = set()
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            # Calculamos la suma (doble del punto medio) para mantener enteros precisos
            sum_x = x1 + x2
            sum_y = y1 + y2
            midpoint = (sum_x, sum_y)
            
            if midpoint in vistos:
                print("YES")
                return
            vistos.add(midpoint)
            
    print("NO")

if __name__ == '__main__':
    solve()