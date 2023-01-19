from _collections import deque

substrings = deque(str(x) for x in input().split())
matching_colors = ['red', 'blue', 'yellow', 'orange', 'green', 'purple']
colors = []

secondary_colors = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']
}

while substrings:
    first = substrings.popleft()
    second = substrings.pop() if substrings else ''
    first_comb = first + second
    second_comb = second + first
    if first_comb in matching_colors:
        colors.append(first_comb)
        continue
    elif second_comb in matching_colors:
        colors.append(second_comb)
        continue
    else:
        for el in (first[:-1], second[:-1]):
            if el:
                substrings.insert(len(substrings) // 2, el)

for color in colors:
    if color in secondary_colors:
        if not set(secondary_colors[color]).issubset(colors):
            colors.remove(color)

print(colors)
