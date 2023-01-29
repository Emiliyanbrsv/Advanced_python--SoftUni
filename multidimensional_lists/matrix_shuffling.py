def validation_and_swap_func(info, r, c, curr_matrix):
    command = info.split()
    action = command.pop(0)
    if action == 'swap' and len(command) == 4:
        number_int = [int(x) for x in command]
        row1, col1, row2, col2 = number_int
        if 0 <= int(row1) < r and 0 <= int(row2) < r and \
                0 <= int(col1) < c and 0 <= int(col2) < c:
            curr_matrix[row1][col1], curr_matrix[row2][col2] = curr_matrix[row2][col2], curr_matrix[row1][col1]
            return True


rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

while True:
    main_command = input()
    if main_command == 'END':
        break

    if validation_and_swap_func(main_command, rows, cols, matrix):
        for mtx in matrix:
            print(*mtx)
    else:
        print('Invalid input!')
