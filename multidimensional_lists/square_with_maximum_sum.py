from sys import maxsize

rows, cols = list(map(int, input().split(', ')))
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

biggest_sum = -maxsize
biggest_matrix_sum = []

for r in range(rows - 1):
    for c in range(cols - 1):
        current_sum = 0
        current_sum += matrix[r][c] + matrix[r][c + 1] + matrix[r + 1][c] + matrix[r + 1][c + 1]
        if current_sum > biggest_sum:
            biggest_sum = current_sum
            biggest_matrix_sum = [[matrix[r][c], matrix[r][c + 1]], [matrix[r + 1][c], matrix[r + 1][c + 1]]]

for curr_matrix in biggest_matrix_sum:
    print(*curr_matrix)
print(biggest_sum)
