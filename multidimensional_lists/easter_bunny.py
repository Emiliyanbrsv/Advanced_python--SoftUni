size = int(input())
matrix = []

bunny_pos = []
best_direction = None
total_eggs = 0
best_route = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    matrix.append(input().split())

    if 'B' in matrix[row]:
        bunny_pos = [row, matrix[row].index('B')]

for direction, position in directions.items():
    row, col = [
        bunny_pos[0] + position[0],
        bunny_pos[1] + position[1]
    ]
    curr_path = []
    curr_eggs = 0

    while 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == 'X':
            break

        curr_path.append([row, col])
        curr_eggs += int(matrix[row][col])

        row += position[0]
        col += position[1]
    if curr_eggs >= total_eggs:
        total_eggs = curr_eggs
        best_route = curr_path
        best_direction = direction

print(best_direction)
print(*best_route, sep='\n')
print(total_eggs)
