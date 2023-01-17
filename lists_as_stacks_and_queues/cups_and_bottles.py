from collections import deque

cups_capacity = deque([int(x) for x in input().split()])
bottle_capacity = [int(x) for x in input().split()]
waster_water = 0

while True:

    if len(cups_capacity) <= 0 or len(bottle_capacity) <= 0:
        break

    current_bottle = bottle_capacity.pop()
    current_cup = cups_capacity.popleft()
    difference = current_bottle - current_cup
    if current_bottle - current_cup <0:
        cups_capacity.appendleft(abs(difference))
    else:
        waster_water += difference

if bottle_capacity:
    print(f"Bottles: {' '.join([str(x) for x in bottle_capacity])}")
else:
    print(f"Cups: {' '.join([str(x) for x in cups_capacity])}")
print(f"Wasted litters of water: {waster_water}")