from collections import deque

working_bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(str(x) for x in input().split())
total_honey = 0

operators_func = {
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '-': lambda x, y: x - y,
    '+': lambda x, y: x + y
}

while working_bees and nectar:
    current_bee = working_bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar > current_bee:
        symbol = symbols.popleft()
        current_honey = abs(operators_func[symbol](current_bee, current_nectar))
        total_honey += current_honey
    elif current_nectar < current_bee:
        working_bees.appendleft(current_bee)
        continue

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
