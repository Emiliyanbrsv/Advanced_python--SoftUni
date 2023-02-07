def read_matrix_func():
    rows, columns = list(map(int, input().split(', ')))
    current_matrix = []
    for i in range(rows):
        numbers = list(map(int, input().split(', ')))
        current_matrix.append(numbers)
    return current_matrix


matrix = read_matrix_func()
total_sum = sum([sum(x) for x in matrix])
print(total_sum)
print(matrix)
