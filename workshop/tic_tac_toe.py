from collections import deque


def win_check():
    name, symbol = players[0]

    first_diagonal = all([board[i][i] == symbol for i in range(size)])
    second_diagonal = all([board[i][size - i - 1] == symbol for i in range(size)])
    row_check = any([all(pos == symbol for pos in row) for row in board])
    col_check = any([all(board[n][i] == symbol for n in range(size)) for i in range(size)])

    if any([first_diagonal, second_diagonal, row_check, col_check]):
        print(f"{name} won!")
        exit()
    else:
        players.append(players.popleft())
        choose_position()


def symbol_place(pos):
    row = (pos - 1) // size
    col = (pos - 1) % size
    if board[row][col] == ' ':
        board[row][col] = players[0][1]
    else:
        raise ValueError

    [print(f"| {' | '.join(row)} |") for row in board]

    win_check()


def choose_position():
    while True:
        try:
            position = int(input(f"{players[0][0]} choose a free position [1-9]: "))
            if 1 <= position <= 9:
                symbol_place(position)
                break
            else:
                raise ValueError
        except ValueError:
            print(f'{players[0][0]} Enter a valid position')


def start_game():
    player_one = input('Player one name: ')
    player_two = input('Player two name: ')
    while True:
        first_player_symbol = input(f"{player_one} would you like to play with 'X' or 'O'? ").upper()
        if first_player_symbol not in ['X', 'O']:
            print(f'{player_one} please enter a valid symbol!')
            continue
        else:
            break
    second_player_symbol = 'X' if first_player_symbol == 'O' else 'O'

    players.append([player_one, first_player_symbol])
    players.append([player_two, second_player_symbol])
    print(f"This is the numeration of the board:\n| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |")
    print(f"{player_one} starts first!")

    choose_position()


players = deque()
size = 3
board = [[" ", " ", " "] for _ in range(size)]

start_game()
