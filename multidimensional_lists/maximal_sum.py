import sys

rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

biggest_sum = -sys.maxsize
biggest_matrix = []

for r in range(rows - 2):
    for c in range(cols - 2):

        current_sum = sum(matrix[r][c:c + 3]) + sum(matrix[r + 1][c:c + 3]) + sum(matrix[r + 2][c:c + 3])
        if current_sum > biggest_sum:
            biggest_sum = current_sum
            biggest_matrix = [matrix[r][c:c + 3], matrix[r + 1][c:c + 3], matrix[r + 2][c:c + 3]]
print(f"Sum = {biggest_sum}")
for biggest in biggest_matrix:
    print(*biggest)
