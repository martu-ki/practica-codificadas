import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    base_grid = input_data[2:2+n]
    
    total_size = n ** k
    output = []
    
    # Generamos la grilla iterando sobre cada posición
    for r in range(total_size):
        row_chars = []
        for c in range(total_size):
            curr_r, curr_c = r, c
            is_pixel_hash = True
            # Analizamos de manera descendente el comportamiento fractal en base N
            for _ in range(k):
                rem_r = curr_r % n
                rem_c = curr_c % n
                if base_grid[rem_r][rem_c] == '.':
                    is_pixel_hash = False
                    break
                curr_r //= n
                curr_c //= n
            row_chars.append('#' if is_pixel_hash else '.')
        output.append("".join(row_chars))
        
    print("\n".join(output))

if __name__ == '__main__':
    solve()