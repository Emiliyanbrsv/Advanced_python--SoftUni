matrix = []

for row in range(6):
    matrix.append(input().split())

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

starting_pos = input()
row, col = int(starting_pos[1]), int(starting_pos[4])

while True:
    command = input()

    if command == 'Stop':
        break

    command = command.split(', ')
    type_command, direction = command[0], command[1]

    row, col = [
        row + directions[direction][0],
        col + directions[direction][1]
    ]

    if type_command == 'Create':
        value = command[2]
        if matrix[row][col] == '.':
            matrix[row][col] = value

    elif type_command == 'Update':
        value = command[2]
        if matrix[row][col] != '.':
            matrix[row][col] = value

    elif type_command == 'Delete':
        if matrix[row][col] != '.':
            matrix[row][col] = '.'
    elif type_command == 'Read':

        if matrix[row][col] != '.':
            print(matrix[row][col])

for row in matrix:
    print(*row)
