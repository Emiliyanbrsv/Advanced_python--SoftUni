def read_matrix_func():
    rows = int(input())
    matrix = []
    for i in range(rows):
        numbers = [int(x) for x in input().split(', ')]
        matrix.append(numbers)
    return matrix


final_matrix = read_matrix_func()
result = []
for matrix in final_matrix:
    result.extend(matrix)
print(result)
