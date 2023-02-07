rows, cols = [int(x) for x in input().split()]

start = ord('a')
matrix = []
for r in range(rows):
    current_matrix = []
    for c in range(cols):
        current_matrix.append(f"{chr(start+r)}{chr(start+r+start+c-start)}{chr(start+r)}")

    matrix.append(current_matrix)

for mtx in matrix:
    print(*mtx)