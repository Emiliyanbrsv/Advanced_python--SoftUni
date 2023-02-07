rows, cols = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

for c in range(cols):
    current_sum = 0
    for r in range(rows):
        current_sum += matrix[r][c]
    print(current_sum)
