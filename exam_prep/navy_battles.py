size = int(input())
battlefield = []

ship_pos = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

bombs_blown = 0
battle_cruiser = 3

for i in range(size):
    row = list(input())
    battlefield.append(row)

    if 'S' in row:
        ship_pos = [i, battlefield[i].index('S')]
        battlefield[ship_pos[0]][ship_pos[1]] = '-'
while bombs_blown < 3 and battle_cruiser > 0:
    command = input()
    row, col = [
        ship_pos[0] + directions[command][0],
        ship_pos[1] + directions[command][1]
    ]
    if battlefield[row][col] == 'C':
        battle_cruiser -= 1
    elif battlefield[row][col] == '*':
        bombs_blown += 1
    battlefield[ship_pos[0]][ship_pos[1]] = '-'
    ship_pos = [row, col]
battlefield[ship_pos[0]][ship_pos[1]]='S'

if battle_cruiser == 0:
    print('Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')
elif bombs_blown ==3:
    print(f"Mission failed, U-9 disappeared! Last known coordinates {[ship_pos[0], ship_pos[1]]}!")

[print(''.join(x)) for x in battlefield]