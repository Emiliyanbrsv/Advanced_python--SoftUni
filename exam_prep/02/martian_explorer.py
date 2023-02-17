def check_index(row_check, col_check):
    if row_check == -1:
        row_check = SIZE - 1
    elif row_check == SIZE:
        row_check = 0
    elif col_check == -1:
        col_check = SIZE - 1
    elif col_check == SIZE:
        col_check = 0

    return row_check, col_check


SIZE = 6
matrix = []
rover_pos = []

deposits = {
    'W': ['Water deposit', 0],
    'M': ['Metal deposit', 0],
    'C': ['Concrete deposit', 0],
}

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(SIZE):
    matrix.append(input().split())

    if 'E' in matrix[row]:
        rover_pos = [row, matrix[row].index('E')]

rover_directions = input().split(', ')

for direction in rover_directions:
    r = rover_pos[0] + directions[direction][0]
    c = rover_pos[1] + directions[direction][1]

    r, c = check_index(r, c)

    if matrix[r][c] == 'R':
        print(f'Rover got broken at {(r, c)}')
        break
    elif matrix[r][c] in deposits.keys():
        deposits[matrix[r][c]][1] += 1
        print(f"{deposits[matrix[r][c]][0]} found at {(r, c)}")
        matrix[r][c] = '-'

    rover_pos = [r, c]

suitable_area = set()
for deposit in deposits.values():
    if deposit[1] >= 1:
        suitable_area.add(True)
    else:
        suitable_area.add(False)

if False not in suitable_area:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
