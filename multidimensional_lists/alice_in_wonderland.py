size = int(input())
matrix = []

alice_pos = []
total_tea_bags = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    matrix.append(input().split())

    if 'A' in matrix[row]:
        alice_pos = [row, matrix[row].index('A')]
        matrix[row][matrix[row].index('A')] = '*'

while total_tea_bags < 10:
    direct = input()
    row, col = [
        alice_pos[0] + directions[direct][0],
        alice_pos[1] + directions[direct][1]
    ]
    if 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == 'R':
            matrix[row][col] = '*'
            break
        elif matrix[row][col].isdigit():
            total_tea_bags += int(matrix[row][col])

        matrix[row][col] = '*'

        alice_pos[0] = row
        alice_pos[1] = col
    else:
        break

if total_tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for r in matrix:
    print(*r)
