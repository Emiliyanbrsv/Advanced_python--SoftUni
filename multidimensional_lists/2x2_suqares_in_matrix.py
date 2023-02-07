rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows)]

identical_counter = 0

for r in range(rows - 1):
    for c in range(cols - 1):
        if matrix[r][c] == matrix[r][c + 1] == matrix[r + 1][c] == matrix[r + 1][c + 1]:
            identical_counter += 1

print(identical_counter)
