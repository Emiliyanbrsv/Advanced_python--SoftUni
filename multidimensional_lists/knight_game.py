size = int(input())
matrix = [[x for x in input()] for _ in range(size)]

positions = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (1, -2),
    (-1, 2),
    (1, 2),
    (2, -1),
    (2, 1)
)

removed_knights = 0

while True:
    max_attack = 0
    biggest_knight_attack = []

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == 'K':
                current_attack = 0

                for pos in positions:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_row < size and 0 <= pos_col < size:
                        if matrix[pos_row][pos_col] == 'K':
                            current_attack += 1

                if current_attack > max_attack:
                    max_attack = current_attack
                    biggest_knight_attack = [row, col]
    if biggest_knight_attack:
        removed_knights += 1
        r, c = biggest_knight_attack
        matrix[r][c] = 0
    else:
        break
print(removed_knights)
