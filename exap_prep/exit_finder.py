player1, player2 = input().split(', ')
size = 6
matrix = []

for row in range(size):
    matrix.append(input().split())

start_index = 1
players1_is_rested = False
players2_is_rested = False

while True:
    coordinates = input()
    row = int(coordinates[1])
    col = int(coordinates[4])
    curr_player = ''

    if (start_index + 1) % 2 == 0:
        if not players1_is_rested:
            if matrix[row][col] == 'E':
                print(f"{player1} found the Exit and wins the game!")
                break
            elif matrix[row][col] == 'T':
                print(f"{player1} is out of the game! The winner is {player2}.")
                break
            elif matrix[row][col] == 'W':
                print(f"{player1} hits a wall and needs to rest.")
                players1_is_rested = True
                start_index += 1
                continue
        else:
            players1_is_rested = False
            start_index += 1
            continue

    elif (start_index + 1) % 2 != 0:
        if not players2_is_rested:
            if matrix[row][col] == 'E':
                print(f"{player2} found the Exit and wins the game!")
                break
            elif matrix[row][col] == 'T':
                print(f"{player2} is out of the game! The winner is {player1}.")
                break
            elif matrix[row][col] == 'W':
                print(f"{player2} hits a wall and needs to rest.")
                players2_is_rested = True
                start_index += 1
                continue
        else:
            players2_is_rested = False
            start_index += 1
            continue
    start_index += 1
