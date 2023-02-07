field = []
our_pos = []
total_targets = 0
targets_index = []
targets_hit = 0
COMMAND_MOVE = 'move'
COMMAND_SHOOT = 'shoot'

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(5):
    field.append(input().split())

    if 'A' in field[row]:
        our_pos = [row, field[row].index('A')]
    if 'x' in field[row]:
        total_targets += field[row].count('x')

iterations = int(input())
for _ in range(iterations):
    command = input().split()
    type_command, direction = command[0], command[1]

    if type_command == COMMAND_MOVE:
        steps = int(command[2])
        row = our_pos[0] + (directions[direction][0] * steps)
        col = our_pos[1] + (directions[direction][1] * steps)
        if 0 <= row < 5 and 0 <= col < 5 and field[row][col] == '.':
            our_pos = [row, col]

    elif type_command == COMMAND_SHOOT:
        row = our_pos[0] + directions[direction][0]
        col = our_pos[1] + directions[direction][1]
        while 0 <= row < 5 and 0 <= col < 5:
            if field[row][col] == 'x':
                field[row][col] = '.'
                total_targets -= 1
                targets_hit += 1
                targets_index.append([row, col])
                break
            else:
                row += directions[direction][0]
                col += directions[direction][1]
    if total_targets == 0:
        print(f"Training completed! All {targets_hit} targets hit.")
        break

if total_targets > 0:
    print(f"Training not completed! {total_targets} targets left.")

[print(target) if target else None for target in targets_index]
