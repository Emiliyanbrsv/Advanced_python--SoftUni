presents = int(input())
size = int(input())
neighborhood = []

santa_pos = []
nice_kids = 0
total_nice_kids = 0

directions = {
    'left': (0, -1),
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0)
}

for row in range(size):
    neighborhood.append(input().split())

    if 'S' in neighborhood[row]:
        santa_pos = [row, neighborhood[row].index('S')]
    if 'V' in neighborhood[row]:
        total_nice_kids += neighborhood[row].count('V')

while True:
    command = input()
    if command == 'Christmas morning':
        break

    r = santa_pos[0] + directions[command][0]
    c = santa_pos[1] + directions[command][1]

    if 0 <= r < size and 0 <= c < size:
        if neighborhood[r][c] == 'V':
            total_nice_kids -= 1
            nice_kids += 1
            presents -= 1
            neighborhood[r][c] = 'S'
            neighborhood[santa_pos[0]][santa_pos[1]] = '-'
            santa_pos[0], santa_pos[1] = r, c

        elif neighborhood[r][c] == 'C':
            neighborhood[r][c] = 'S'
            neighborhood[santa_pos[0]][santa_pos[1]] = '-'
            santa_pos[0], santa_pos[1] = r, c
            for direction in directions.values():
                r += direction[0]
                c += direction[1]
                if 0 <= r < size and 0 <= c < size:

                    if neighborhood[r][c] == 'V':
                        total_nice_kids -= 1
                        nice_kids += 1
                        presents -= 1
                        neighborhood[r][c] = '-'
                    elif neighborhood[r][c] == 'X':
                        presents -= 1
                        neighborhood[r][c] = '-'
                    if presents == 0:
                        break
                r, c = santa_pos[0], santa_pos[1]
        else:
            neighborhood[r][c] = 'S'
            neighborhood[santa_pos[0]][santa_pos[1]] = '-'
            santa_pos[0], santa_pos[1] = r, c
        if presents == 0:
            break
if presents == 0 and total_nice_kids !=0:
    print(f"Santa ran out of presents!")
[print(*rows) if rows else None for rows in neighborhood]
if total_nice_kids ==0:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids} nice kid/s.")