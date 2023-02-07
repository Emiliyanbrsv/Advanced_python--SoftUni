def read_matrix_func():
    rows = int(input())
    matrix = []
    for i in range(rows):
        numbers = [int(x) for x in input().split(', ') if int(x) % 2 == 0]
        matrix.append(numbers)
    return matrix


final_matrix = read_matrix_func()
print(final_matrix)
