size = int(input())
car_number = input()
tunnel = []
matrix = []
kilometers = 0
car_pos = [0, 0]
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
for row in range(size):
    matrix.append(input().split())
    if 'T' in matrix[row]:
        tunnel = [row, matrix[row].index('T')]

while True:
    command = input()
    if command == 'End':
        print(f"Racing car {car_number} DNF.")
        matrix[car_pos[0]][car_pos[1]] = 'C'
        break

    r = (car_pos[0] + directions[command][0])
    c = (car_pos[1] + directions[command][1])
    if 0 <= r < size and 0 <= c < size:
        kilometers += 10
        if matrix[r][c] == 'T':
            kilometers += 20
            car_pos = [tunnel[0], tunnel[1]]
            matrix[tunnel[0]][tunnel[1]] = '.'
        elif matrix[r][c] == 'F':
            print(f"Racing car {car_number} finished the stage!")
            matrix[r][c] = 'C'
            break
        else:
            car_pos[0]=r
            car_pos[1]=c
        matrix[r][c] = '.'

print(f"Distance covered {kilometers} km.")
for rows in matrix:
    print(''.join(rows))