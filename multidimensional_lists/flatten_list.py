line = input().split("|")
reversed_line = []

for data in line[::-1]:
    reversed_line.extend(data.split())
print(*reversed_line)
