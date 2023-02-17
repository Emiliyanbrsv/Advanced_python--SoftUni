from math import floor


def check_index(row_check, col_check, num):
    if row_check == -1:
        row_check = num - 1
    elif row_check == num:
        row_check = 0
    elif col_check == -1:
        col_check = num - 1
    elif col_check == num:
        col_check = 0

    return row_check, col_check


size = int(input())
matrix = []
path = []
player_pos = []
coins = 0
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    matrix.append(input().split())

    if 'P' in matrix[row]:
        player_pos = [row, matrix[row].index('P')]
        path.append([row, matrix[row].index('P')])
while True:
    if coins >= 100:
        print(f"You won! You've collected {coins} coins.")
        break
    direction = input()
    r = player_pos[0] + directions[direction][0]
    c = player_pos[1] + directions[direction][1]

    r, c = check_index(r, c, size)
    path.append([r, c])
    if matrix[r][c].isdigit():
        coins += int(matrix[r][c])
        matrix[r][c] = '0'
    elif matrix[r][c] == 'X':
        coins /= 2
        print(f"Game over! You've collected {floor(coins)} coins.")
        break

    player_pos = [r, c]
print('Your path:')
print(*path, sep='\n')
