n = int(input())

matrix = [[x for x in input()] for _ in range(n)]
special_symbol = input()
symbol_cord = []
found_symbol = False
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        current_symbol = matrix[row][col]
        if current_symbol == special_symbol:
            symbol_cord = (row, col)
            found_symbol = True
        if found_symbol:
            break
    if found_symbol:
        break

if found_symbol:
    print(f"{symbol_cord}")
else:
    print(f"{special_symbol} does not occur in the matrix")
