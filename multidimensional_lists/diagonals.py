n = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]

primary_diagonal = []
secondary_diagonal = []
for row in range(n):
    primary_diagonal.append(matrix[row][row])
    secondary_diagonal.append(matrix[::-1][row][row])

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal[::-1]])}. Sum: {sum(secondary_diagonal)}")
