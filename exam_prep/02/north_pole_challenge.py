rows, cols = [int(x) for x in input().split(', ')]
matrix = []
santa_pos = []

christmas_decorations = 0
christmas_decorations_collected = 0
gifts = 0
gifts_collected = 0
cookies = 0
cookies_collected = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(rows):
    matrix.append(input().split())

    if 'Y' in matrix[row]:
        santa_pos = [row, matrix[row].index('Y')]
        matrix[santa_pos[0]][santa_pos[1]] = 'x'
    if 'D' in matrix[row]:
        christmas_decorations += matrix[row].count('D')
    if 'G' in matrix[row]:
        gifts += matrix[row].count('G')
    if 'C' in matrix[row]:
        cookies += matrix[row].count('C')

while True:
    command = input()
    if command == 'End':
        break

    command = command.split('-')
    direction, steps = command[0], int(command[1])
    r = santa_pos[0]
    c = santa_pos[1]

    while steps > 0:
        if direction == 'left':
            c -= 1
            steps -= 1
            if c < 0:
                c = cols - 1
        elif direction == 'right':
            c += 1
            steps -= 1
            if c >= cols:
                c = 0
        elif direction == 'up':
            r -= 1
            steps -= 1
            if r < 0:
                r = rows - 1
        elif direction == 'down':
            r += 1
            steps -= 1
            if r >= rows:
                r = 0

        if matrix[r][c] == 'D':
            christmas_decorations -= 1
            christmas_decorations_collected += 1
        elif matrix[r][c] == 'G':
            gifts -= 1
            gifts_collected += 1
        elif matrix[r][c] == 'C':
            cookies -= 1
            cookies_collected += 1

        matrix[r][c] = 'x'
        santa_pos = [r, c]

        if christmas_decorations + cookies + gifts == 0:
            break

    if christmas_decorations + cookies + gifts == 0:
        print('Merry Christmas!')
        break
matrix[santa_pos[0]][santa_pos[1]] = 'Y'

print("You've collected:")
print(f"- {christmas_decorations_collected} Christmas decorations")
print(f"- {gifts_collected} Gifts")
print(f"- {cookies_collected} Cookies")

for row in matrix:
    print(*row)
