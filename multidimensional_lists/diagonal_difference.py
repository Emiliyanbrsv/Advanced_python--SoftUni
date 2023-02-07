n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

primary = []
secondary = []

for r in range(n):
    primary.append(matrix[r][r])

for r in range(n - 1, -1, -1):
    secondary.append(matrix[r][n-r-1])

print(abs(sum(primary) - sum(secondary)))
