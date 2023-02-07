size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]

COMMAND_ADD = 'Add'
COMMAND_SUBTRACT = 'Subtract'
COMMAND_END = 'END'

while True:
    command = input().split()

    if command[0] == COMMAND_END:
        break

    type_command, row, col, num = command[0], int(command[1]), int(command[2]), int(command[3])

    if 0 <= row < size and 0 <= col < size:
        if type_command == COMMAND_ADD:
            matrix[row][col] += num
        elif type_command == COMMAND_SUBTRACT:
            matrix[row][col] -= num
    else:
        print('Invalid coordinates')

[print(*row) for row in matrix]